from django.db import models
from django.urls import reverse
# Create your models here.

class Genere(models.Model):

    nome = models.CharField(max_length = 20)

    class Meta:
        verbose_name = "Genere"
        verbose_name_plural = "Generi"

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("lista_libri_per_genere", kwargs={"pk":self.pk})

class Autore(models.Model):

    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)
    nazione = models.CharField(max_length = 20)

    class Meta:
        verbose_name = "Autore"
        verbose_name_plural = "Autori"

    def __str__(self):
        return self.nome + " " + self.cognome

    def get_absolute_url(self):
        return reverse("dettaglio_autore", kwargs={"pk":self.pk})


class Libro(models.Model):

    titolo = models.CharField(max_length = 60)
    autore = models.ForeignKey(Autore, on_delete=models.CASCADE, related_name="libri")
    genere = models.ManyToManyField(Genere, related_name="libri")
    tipoCopertina = models.CharField(max_length = 40, blank=True, null=True)
    descrizione = models.TextField(blank=True, null=True)
    #genere = models.ForeignKey("Genere", on_delete=models.CASCADE)
    isbn = models.CharField(max_length = 20)

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libri"

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse("dettaglio_libro", kwargs={"pk":self.pk})
