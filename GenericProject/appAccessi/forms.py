from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormRegistrazione(UserCreationForm):
    #Nel corso aggiungiamo alla UserCreationForm (solo username + pwd anche il campo email come segue)
    #email = forms.CharField(max_length = 50, required = True, widget = forms.EmailInput())
    #Da verificare cosa cambia specificando direttamente il tipo EmailField invece che widget = EmailInput()
    email = forms.EmailField(max_length=50, required=True)
    first_name = forms.CharField(max_length=30, required=True, label='Nome')
    last_name = forms.CharField(max_length=30, required=True, label='Cognome')

    class Meta:
        model = User
        fields = ["first_name","last_name","username", "email", "password1", "password2"]
