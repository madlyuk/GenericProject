from django import forms
#from django.core import validators
#from django.core.exceptions import ValidationError
from .models import Contatti

class FormContatti(forms.ModelForm):
    class Meta:
        model = Contatti
        #fields = ["nome","cognome","email","oggetto","contenuto"]
        fields = '__all__'
