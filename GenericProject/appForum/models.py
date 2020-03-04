from django.db import models
from django.contrib.auth.models import User
#LE importazioni di seguito servono per i metodi che mostreranno la preview del logo in admin (adminmodels)
import os
from django.conf import settings
from django.utils.safestring import mark_safe
from django.urls import reverse
from math import ceil

# Create your models here.

class Sezione(models.Model):
    """
    Le Sezioni permettono di suddividere le discussioni in aree tematiche e sono create solo da chi ha particolari privilegi
    """
    titolo = models.CharField(max_length = 100)
    descrizione = models.CharField(max_length = 200, blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.titolo

    def url(self):
        return os.path.join('/',settings.MEDIA_URL, os.path.basename(str(self.logo)))

    def logo_image_preview(self,dim=64):
        admin_width_preview_image = dim
        admin_heigth_preview_image = dim
        return mark_safe(f'<img src="{self.url()}" width="{admin_width_preview_image}" height="{admin_heigth_preview_image}" />' )
    logo_image_preview.short_description = 'Logo'

    def get_absolute_url(self):
        return reverse("dettaglio_sezione",kwargs={"pk":self.pk})

    def get_last_discussions(self):
        return Discussione.objects.filter(sezione=self).order_by("-data_creazione")[:2]

    #Query complessa: siamo nella classe sezione e cerco tutti i Posts filtrati per parametro discussione, ovvero per tutte quelle discussioni che hanno come attributo sezione Self (la sezione istanziata)
    def get_num_of_posts_in_section(self):
        return Post.objects.filter(discussione__sezione = self).count()

    class Meta:
        verbose_name="Sezione"
        verbose_name_plural="Sezioni"


class Discussione(models.Model):
    """
    Le Discussioni possono essere aperte da tutti gli user e raccolgono i vari post degli utenti
    """
    titolo = models.CharField(max_length = 100)
    data_creazione = models.DateTimeField(auto_now_add=True)
    autore = models.ForeignKey(User, on_delete=models.CASCADE, related_name="discussioni")
    sezione = models.ForeignKey(Sezione, on_delete=models.CASCADE, related_name="discussioni_sezione")

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse("dettaglio_discussione", kwargs={"pk":self.pk})

    def get_num_of_posts_in_discussion(self):
        return Post.objects.filter(discussione = self).count()

    def get_last_post_in_discussion(self):
        return Post.objects.filter(discussione = self).last()

    def get_num_pages(self):
        #num_posts = self.post_set.count()
        num_posts = self.get_num_of_posts_in_discussion()
        num_pages = ceil(num_posts/5)
        return num_pages

    class Meta:
        verbose_name="Discussione"
        verbose_name_plural="Discussioni"

class Post(models.Model):
    """
    Sono i messaggi degli utenti all'interno delle discussioni
    """
    contenuto = models.TextField()
    data_creazione = models.DateTimeField(auto_now_add=True)
    autore = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    discussione = models.ForeignKey(Discussione, on_delete=models.CASCADE, related_name="discussioni")


    def __str__(self):
        return self.autore.username + " - " + str(self.data_creazione)

    def get_short_description(self):
        return self.contenuto [:50] +"..."
    get_short_description.short_description="Estratto"

    class Meta:
        verbose_name="Post"
        verbose_name_plural="Posts"
