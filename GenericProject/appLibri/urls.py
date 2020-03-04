"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import GenereListViewCB,AutoreListViewCB,LibroListViewCB,catalogo_libri,LibroDetailViewCB,AutoreDetailViewCB,GenereDetailViewCB

urlpatterns = [
    #path('lista_generi', GenereListViewCB.as_view(), name='lista_generi')
    path('catalogo', catalogo_libri, name='catalogo_libri'),
    path('lista_generi', GenereListViewCB.as_view(), name='lista_generi'),
    path('lista_autori', AutoreListViewCB.as_view(), name='lista_autori'),
    path('lista_libri', LibroListViewCB.as_view(), name='lista_libri'),
    path('dettaglio_autore/<int:pk>', AutoreDetailViewCB.as_view(), name='dettaglio_autore'),
    path('dettaglio_libro/<int:pk>', LibroDetailViewCB.as_view(), name='dettaglio_libro'),
    path('lista_libri_per_genere/<int:pk>', GenereDetailViewCB.as_view(), name='lista_libri_per_genere')

]
