from django.contrib import admin
from .models import Sezione, Discussione, Post
# Register your models here.

class SezioneModelAdmin(admin.ModelAdmin):
    model = Sezione
    list_display = ['id','titolo','logo_image_preview']
    search_fields =['titolo']


class DiscussioneModelAdmin(admin.ModelAdmin):
    model = Discussione
    list_display = ['id','titolo','sezione','autore','data_creazione']
    search_fields =['titolo','autore']
    list_filter = ['sezione','data_creazione']

class PostModelAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['id','get_short_description','discussione','autore','data_creazione']
    search_fields =['contenuto','autore__username']
    list_filter = ['discussione','autore','data_creazione']

admin.site.register(Sezione,SezioneModelAdmin)
admin.site.register(Discussione,DiscussioneModelAdmin)
admin.site.register(Post,PostModelAdmin)
