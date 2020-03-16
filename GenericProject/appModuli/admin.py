from django.contrib import admin
from .models import AppModuli


class appModuliModelAdmin(admin.ModelAdmin):
    model = AppModuli
    list_display = ['title','visible','enabled']


# Register your models here.
admin.site.register(AppModuli,appModuliModelAdmin)
