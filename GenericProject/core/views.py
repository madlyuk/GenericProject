from django.shortcuts import render, redirect, get_object_or_404
from appModuli.models import AppModuli
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Permission
from appForum.models import Post, Discussione
from products.models import Product, Manufacturer
from appModuli.models import AppModuli
from django.db.models import Q

class UserListViewCB(LoginRequiredMixin,ListView):
    model = User
    template_name = 'users/lista_utenti.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['appForum'] = AppModuli.objects.get(title="Forum");
        return context

# Create your views here.

def homepage(request):
    appList = AppModuli.objects.all()
    context = {"appList":appList}
    return render(request,"core/home.html",context)

def userProfileView(request, username):
    user = get_object_or_404(User, username=username)
    permissions = User.get_group_permissions(user)
    context = {'user':user, 'permissions':permissions}
    appForum = AppModuli.objects.get(title="Forum")
    posts_utente = Post.objects.filter(autore=user)
    context.update({'posts_utente':posts_utente})
    context.update({'appForum':appForum})
    return render(request,"users/profilo_utente.html", context)

def userProfileView_ORIGINALE_CORSO(request, username):
    user = get_object_or_404(User, username=username)
    discussioni_utente = Discussione.objects.filter(autore=user).order_by("-pk")
    context = {"user": user, "discussioni_utente": discussioni_utente}
    return render(request, 'users/profilo_utente.html', context)

# Ho utilizzato una generica class-base ListView
# def userListView_temp(request):
#     users = User.objects.all()
#     context = {'users':users}
#     return render(request,"users/lista_utenti.html", context)


def cerca(request):
    if "q" in request.GET:
        querystring = request.GET.get("q")
        if len(querystring) == 0:
            return redirect("/cerca/")
        
        #Cerca tra gli utenti
        appUtenti = AppModuli.objects.get(title="Autenticazione")
        users = User.objects.filter(
            Q(username__icontains = querystring) |
            Q(last_name__icontains = querystring) |
            Q(first_name__icontains = querystring)
        )
        context = {"users":users, "appUtenti":appUtenti}

        #Cerca nel Forum
        appForum = AppModuli.objects.get(title="Forum")
        discussioni = Discussione.objects.filter(titolo__icontains = querystring)
        contenuto_posts = Post.objects.filter(contenuto__icontains = querystring)
        context.update({"discussioni":discussioni, "contenuto_posts":contenuto_posts, "appForum": appForum})

        #Cerca Tra i prodotti
        appProducts = AppModuli.objects.get(title="Catalogo Prodotti")
        products = Product.objects.filter(Q(name__icontains = querystring) |
                                          Q(description__icontains = querystring)
                                        )
        manufacturer = Manufacturer.objects.filter(name__icontains = querystring)
        context.update({"products":products, "manufacturer":manufacturer, "appProducts":appProducts})

        return render(request, "core/cerca.html", context)
    else:
        return render(request, "core/cerca.html")
