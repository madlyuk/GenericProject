from django.db import models

# Create your models here.

class AppModuli(models.Model):
    title = models.CharField(max_length=20);
    desc = models.TextField();
    image = models.CharField(max_length=200);
    visible = models.BooleanField(default=False);
    enabled = models.BooleanField(default=True);
    mainAppView = models.CharField(max_length=100, verbose_name="main View",blank=True,null=True);

    def __str__(self):
        return self.title

    def is_visible(self):
        return self.visible == True

    def is_enabled(self):
        return self.enabled == True

    def checkAppActivation(self,appTitle):
        app = AppModuli.objects.get(title=appTitle)
        return app.is_visible and app.is_enabled

    class Meta:
        verbose_name = "AppModuli"
        verbose_name_plural = "AppModuli"
