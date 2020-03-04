from django.db import models

# Create your models here.
class Contatti(models.Model):
    nome = models.CharField(max_length = 30)
    cognome = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 50)
    oggetto = models.CharField(max_length = 100)
    contenuto = models.TextField(max_length = 500)

    class Meta:
        verbose_name_plural = "Contatti"


    def __str__(self):
        return str(self.email) + " - " + str(self.oggetto) 
