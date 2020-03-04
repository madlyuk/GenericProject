
from django.urls import path
from .views import eventList
from .views import eventTypeList, eventTypeDetails


urlpatterns = [
    path('lista_eventi', eventList, name='eventList'),
    path('dettaglio_tipo_eventi/<int:pk>', eventTypeDetails, name='eventTypeDetails'),
    path('lista_tipo_eventi', eventTypeList, name='eventTypeList')
]
