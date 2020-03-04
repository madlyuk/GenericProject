from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import *


def eventList(request):
    eventList = Event.objects.all()
    eventTypeList = EventType.objects.all()
    eventRegulatoryList = EventRegulatory.objects.all()
    eventTrainingChannelList = EventTrainingChannel.objects.all()
    context = {"eventList":eventList, "eventTypeList":eventTypeList, "eventRegulatoryList":eventRegulatoryList, "eventTrainingChannelList": eventTrainingChannelList}
    return render(request,"event_list.html",context)

def eventTypeList(request):
    evtType = EventType.objects.all()
    context = {"eventTypeList":evtType}
    template = "event_type_list.html"
    return render(request, template, context)

def eventTypeDetails(request, pk):
    evtType = get_object_or_404(EventType, pk=pk)
    context = {"eventTypeDetails":evtType}
    return render(request, "event_type_details.html", context)
