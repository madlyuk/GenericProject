"""GenericProject.urls URL Configuration

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    #path('', include('appBlog.urls')),
    path('libri/', include('appLibri.urls')),
    path('eventi/', include('appEventi.urls')),
    path('app/', include('appModuli.urls')),
    path('contatti/', include('appContatti.urls')),
    path('accounts/', include('appAccessi.urls')),
    path('forum/', include('appForum.urls')),
    path('prodotti/', include('products.urls'))
]

#Django non permette, in sviluppo (debug), un accesso diretto alle immagini caricate.
#Per acedere tramite MEDIA_URL, dobbiamo mapparlo (2) nel file urls.py di progetto
#faccendo riferimento a MEDIA_ROOT e MEDIA_URL definiti nel file di settings (1)
#per questo motivo dobbiamo importare le seguenti librerie
from django.conf import settings #(1)
from django.conf.urls.static import static #(2)

#questa modifica per accedere ai media-file in fase di sviluppo è descritta nei commenti del metodo "static" (qui sotto). Si puo' accedere alla definizione tramite CMD+ALT+g
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
