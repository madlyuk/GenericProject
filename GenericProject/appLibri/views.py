from django.shortcuts import render, get_object_or_404
from .models import Genere, Autore, Libro

# Create your views here.


def catalogo_libri(response):
    libri = Libro.objects.all()
    context = {"libri":libri}
    return render(response,"catalogo_libri.html",context)


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class GenereListViewCB(ListView):

    model = Genere
    template_name = "lista_generi.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["generi"] = Genere.objects.all()
        return context

class AutoreListViewCB(ListView):

    model = Autore
    template_name = "lista_autori.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["autori"] = Autore.objects.all()
        return context

    

class LibroListViewCB(ListView):

    model = Libro
    template_name = "lista_libri.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["libri"] = Libro.objects.all()
        return context

class AutoreDetailViewCB(DetailView):

    model = Autore
    template_name = "dettaglio_autore.html"

    def get(self, request, *args, **kwargs):
        autore = get_object_or_404(Autore, pk=kwargs['pk'])
        context = {'autore': autore}
        return render(request, './dettaglio_autore.html', context)


class GenereDetailViewCB(DetailView):

    model = Genere
    template_name = "lista_libri_per_genere.html"

    def get(self, request, *args, **kwargs):
        genere = get_object_or_404(Genere, pk=kwargs['pk'])
        context = {'genere': genere}
        return render(request, './lista_libri_per_genere.html', context)


class LibroDetailViewCB(DetailView):

    model = Libro
    template_name = "dettaglio_libro.html"

    def get(self, request, *args, **kwargs):
        libro = get_object_or_404(Libro, pk=kwargs['pk'])
        context = {'libro': libro}
        return render(request, './dettaglio_libro.html', context)
