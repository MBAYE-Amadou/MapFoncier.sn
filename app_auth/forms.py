from fonc_app.models import Demandeurs, DemandeursMoral
from django.forms import ModelForm, fields
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Nom utilisateur", widget=forms.TextInput(attrs={'class':'form-control'}))
    pwd = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class':'form-control'}))
 

class DemandeurForm(ModelForm):
    class Meta:
        model =Demandeurs 
        fields =['statut']


class DemandeurMoralForm(ModelForm):
    class Meta:
        model =DemandeursMoral 
        fields =['statut']