from django.contrib.auth.decorators import login_required
from django.core.paginator import Page, Paginator, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse, reverse_lazy
from .models import Sezione, Discussione, Post
from django.contrib.auth.models import User ##agginta per visualizzare i post utente
from .mixins import UserStaffPermissionMixin
from .forms import DiscussioneModelForm, PostModelForm
from appModuli.models import AppModuli


# Create your views here.

########### SEZIONE ################

#Usiamo mixin per specificare che l'accesso alla vista è permesso solo dai membri dello Staff
class CreaSezioneViewCB(UserStaffPermissionMixin,CreateView):
    model=Sezione
    fields="__all__"
    template_name = "appForum/nuova_sezione.html"
    success_url = "/"

class SessionListViewCB(ListView):
    #model = Sezione
    queryset = Sezione.objects.all().order_by('-id');
    template_name = 'appForum/home.html'
    context_object_name = "lista_sezioni" #in questo modo nel template non dobbiamo ciclare sull'object_list

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['appForum'] = AppModuli.objects.get(title="Forum");
        return context

def DettaglioSezioneView(request,pk):
    sezione = get_object_or_404(Sezione, pk=pk)
    discussioni_sezione = Discussione.objects.filter(sezione=sezione).order_by("-data_creazione")
    context = {"sezione":sezione,"discussioni_sezione":discussioni_sezione}
    return render(request, "appForum/dettaglio_sezione.html", context)

########### DISCUSSIONE ################

@login_required
def CreaDiscussioneView(request,pk):
    #dovendo creare non solo una discussione, ma anche un post, preferisco usare una function view
    #il primo step è di inizializzare il form tramite POST, e quindi prima di tutto va creato il form
    #se la chiamata è in post
        #istanzio il form della discussione con i dati passati nel form
        #verifico che sia validate e se validate
            #salvo la discussione mettendola in pausa (no commit) in modo da salvare anche il POST
            #salvo il posto
            #eseguo la commit e renidirizzo ad una pagina di conferma
    #se apro la form (no post)
        #istanzio il form della discussione vuoto
    #definisco il data contest tramite il form della discussione
    #in output il render della richiesta + pagina del form + e il modelform della discussione
    sezione = get_object_or_404(Sezione, pk=pk)
    if request.method == "POST":
        formDiscussione = DiscussioneModelForm(request.POST)
        if formDiscussione.is_valid():
            discussione = formDiscussione.save(commit=False)
            discussione.autore = request.user
            discussione.sezione = sezione
            discussione.save()
            primo_post = Post.objects.create(
                autore=request.user,
                discussione=discussione,
                contenuto=formDiscussione.cleaned_data["contenuto"]
            )
            return HttpResponseRedirect(discussione.get_absolute_url())
    else:
        formDiscussione = DiscussioneModelForm()
    context={"form":formDiscussione, "sezione":sezione}
    return render(request,"appForum/nuova_discussione.html", context)

def DettagliDiscussioneView(request,pk):
    discussione = get_object_or_404(Discussione, pk=pk)
    posts_discussione = Post.objects.filter(discussione=discussione)
    paginator = Paginator(posts_discussione,5)
    page = request.GET.get("pagina")
    posts = paginator.get_page(page)

    form_risposta = PostModelForm()
    context={"discussione":discussione,
             "posts_discussione":posts,
             "form_risposta": form_risposta}
    return render(request, "appForum/dettaglio_discussione.html", context)

########### POST ################
@login_required
def NuovoPostView(request,pk):
    discussione = get_object_or_404(Discussione, pk=pk)
    if request.method == "POST":
        formPost = PostModelForm(request.POST)
        if formPost.is_valid():
            formPost.save(commit=False)
            formPost.instance.discussione = discussione
            formPost.instance.autore = request.user
            formPost.save()
            url_discussione=reverse("dettaglio_discussione",kwargs={'pk':discussione.pk})
            n_pages = discussione.get_num_pages()
            if n_pages > 1:
                url_discussione += "?pagina=" + str(n_pages)
            return HttpResponseRedirect(url_discussione)
    else:
        return HttpResponseBadRequest()

#dai dettagli discussione mettiamo un link anche che riporti a tutti i post per singolo utente
def PostsUtenteView(request,username):
    utente = get_object_or_404(User, username=username)
    posts = Post.objects.filter(autore=utente).order_by('discussione','-data_creazione') #autore=User.username
    context={"posts_utente":posts, 'utente':utente}
    return render(request, "appForum/post_utente.html", context)

class DeletePostView(DeleteView):
    model=Post
    #success_url = reverse_lazy('home_forum')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(autore_id=self.request.user.id)

    def get_success_url(self):
        if 'id' in self.kwargs:
            pk = self.kwargs['id']
        else:
            return self.object.discussione.get_absolute_url()
        return reverse('dettaglio_discussione', kwargs={'pk': pk})


class UpdatePostView(UpdateView):
    model = Post
    fields = ['contenuto']
    template_name_suffix = '_update_form'
    #success_url = self.object.discussione.get_absolute_url()

    def get_success_url(self):
        if 'id' and 'pk' in self.kwargs:
            id = self.kwargs['id']
            pk = self.kwargs['pk']
        else:
            slug = '/'
        #return reverse('modifica_post', kwargs={'id':id, 'pk': pk})
        return self.object.discussione.get_absolute_url()
