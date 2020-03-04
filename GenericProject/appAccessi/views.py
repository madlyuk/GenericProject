from django.shortcuts import render, HttpResponseRedirect
from appAccessi.forms import FormRegistrazione
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
#from django.contrib import messages

def formRegistrazioneView(request):
    if request.method == "POST":
        form = FormRegistrazione(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            email = form.cleaned_data["email"]
            User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password, email=email)
            new_account = authenticate(username=username, password=password)
            login(request, new_account)
            #messages.success(request, 'Registrazione effettuata con successo!')
            return HttpResponseRedirect(f"/")
    else:
        form = FormRegistrazione()
    context = {"form":form}
    return render(request, "registration/registrazione.html", context)






# Create your views here.
