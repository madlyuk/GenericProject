from django.contrib import admin
from .models import Event, EventRegulatory, EventTrainingChannel, EventType
# Register your models here.

admin.site.register(EventRegulatory)
admin.site.register(EventTrainingChannel)
admin.site.register(EventType)
admin.site.register(Event)
