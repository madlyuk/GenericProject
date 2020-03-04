from django.urls import path
from . import views


urlpatterns=[
    path("nuova_sezione",views.CreaSezioneViewCB.as_view(),name="nuova_sezione"),
    path("home",views.SessionListViewCB.as_view(),name="home_forum"),
    path("sezione/<int:pk>",views.DettaglioSezioneView,name="dettaglio_sezione"),
    path("sezione/<int:pk>/nuova_discussione",views.CreaDiscussioneView,name="nuova_discussione"),
    path("discussione/<int:pk>",views.DettagliDiscussioneView,name="dettaglio_discussione"),
    path("discussione/<int:pk>/rispondi",views.NuovoPostView,name="rispondi_a_discussione"),
    path('utente/<username>', views.PostsUtenteView, name='posts_utente'),
    path("discussione/<int:id>/cancella_post/<int:pk>",views.DeletePostView.as_view(),name="cancella_post"),
    path("discussione/<int:id>/modifica_post/<int:pk>",views.UpdatePostView.as_view(),name="modifica_post"),
]
