from django.db import models
from django.urls import reverse

# Create your models here.

class EventTrainingChannel (models.Model):
    """Modello generico relativo al tipo di erogazione degli eventi """
    name = models.CharField(max_length=20)
    shortDesc = models.CharField(max_length=60)
    longDesc = models.TextField()
    enabled = models.BooleanField()

    class Meta:
        ordering = ["name"]
        verbose_name = "Metodo di erogazione"
        verbose_name_plural = "Metodi di erogazione"

    def __str__(self):
        return self.name + " " + self.shortDesc

    def get_absolute_url(self):
        return reverse("eventTrainingChannelDetails", kwargs={"pk":self.pk})

    def isVisible(self):
        return self.enabled

class EventRegulatory (models.Model):
    """Modello generico relativo alla normativa degli eventi erogati"""
    name = models.CharField(max_length=20)
    shortDesc = models.CharField(max_length=60)
    longDesc = models.TextField()
    ruleReference = models.CharField(max_length=100)
    enabled = models.BooleanField()

    class Meta:
        ordering = ["name"]

        verbose_name = "Normativa"
        verbose_name_plural = "Normative"

    def __str__(self):
        return self.name + " " + self.shortDesc

    def get_absolute_url(self):
        return reverse("eventRegulatoryDetails", kwargs={"pk":self.pk})

    def isVisible(self):
        return self.enabled


class EventType (models.Model):
    """Modello generico relativo alla tipologia di evento erogato"""
    name = models.CharField(max_length=20)
    shortDesc = models.CharField(max_length=60)
    longDesc = models.TextField()
    regulatory = models.ForeignKey(EventRegulatory, on_delete=models.CASCADE, related_name="EventType")
    trainingChannel = models.ForeignKey(EventTrainingChannel, on_delete=models.CASCADE, related_name="EventTrainingChannel")
    enabled = models.BooleanField()


    class Meta:
        ordering = ["name"]
        verbose_name = "Tipologia Evento"
        verbose_name_plural = "Tipologie Eventi"


    def __str__(self):
        return self.name + " " + self.shortDesc

    def get_absolute_url(self):
        return reverse("eventTypeDetails", kwargs={"pk":self.pk})

    def isVisible(self):
        #aggiungere anche il controllo sulla visibilità della normativa
        trainingChannel = EventTrainingChannel.objects.get(pk=self.trainingChannel)
        regulatory = EventRegulatory.objects.get(pk=self.regulatory)
        return self.enabled and regulatory.isVisible() and trainingChannel.isVisible()

class Event (models.Model):
    """Modello generico relativo alla tipolgia di evento erogato"""
    name = models.CharField(max_length=20)
    shortDesc = models.CharField(max_length=60)
    longDesc = models.TextField()
    eventType = models.ForeignKey(EventType, on_delete=models.CASCADE, related_name="Event")
    frontend_visible = models.BooleanField()
    backend_visible = models.BooleanField()
    enabled = models.BooleanField()

    class Meta:
        ordering = ["name"]
        verbose_name = "Evento"
        verbose_name_plural = "Eventi"


    def __str__(self):
        return self.name + " " + self.shortDesc

    def get_absolute_url(self):
        return reverse("eventDetails", kwargs={"pk":self.pk})

    def isFrontEndVisible(self):
        #controllo sulla visibilità del tipo di evento
        eventType = EventType.objects.get(pk=self.eventType)
        return self.enabled and self.frontend_visible and eventType.isVisible()

    def isBackEndVisible(self):
        #controllo sulla visibilità del tipo di evento
        eventType = EventType.objects.get(pk=self.eventType)
        return self.enabled and self.backend_visible and eventType.isVisible()
