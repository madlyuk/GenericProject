from .models import Discussione, Post
from django import forms

class DiscussioneModelForm(forms.ModelForm):
    contenuto = forms.CharField(
        widget = forms.Textarea(attrs={"placeholder":"..di cosa vuoi parlare?.."}),
        max_length=4000, label="Primo messaggio"
    )

    class Meta:
        model=Discussione
        fields=["titolo","contenuto"]
        widgets={
            "titolo":forms.Textarea(attrs={"placeholder":"Titolo della discussione",'rows':'2'})
        }

class PostModelForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=["contenuto"]
        widgets={
            'contenuto':forms.Textarea(attrs={'rows':'5'})
        }
        labels={
            'contenuto':"Messaggio"
        }
