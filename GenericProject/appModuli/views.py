from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import AppModuli


def appModuliView(response):
    appList = AppModuli.objects.all()
    context = {"appList":appList}
    return render(response,"appList.html",context)
