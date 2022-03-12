from django.forms import ModelForm, fields, widgets
from .models import Demandeurs, DemandeursMoral
from django import forms


class DemandeursForm(forms.ModelForm):
    class Meta:
        model = Demandeurs
        fields =['Nom', 'Prénom', 'Profession', 
        'Date_de_naissance', 'Sexe', 'Nationalité', 'Adresse_physique', 'Quartier',
        'Téléphone', 'Email', 'Superficie_demandée', 
        'Type_occupation', 'photo'
        ]

        widgets ={
            'Nom':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Votre Nom'}),
            'Prénom':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Votre Prénom'}),
            'Profession':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ce que vous faites'}),
            'Date_de_naissance':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Année-mois-Jour'}),
            'Sexe':forms.Select(attrs={'class':'form-control'}),
            'Nationalité':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sénégalaise'}),
            'Adresse_physique':forms.TextInput(attrs={'class':'form-control', 'placeholder':'adresse'}),
            'Quartier':forms.Select(attrs={'class':'form-control'}),
            'Téléphone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Votre numéro téléphone'}),
            'Email':forms.TextInput(attrs={'class':'form-control', 'placeholder':'email@example.com'}),
            'Superficie_demandée':forms.TextInput(attrs={'class':'form-control', 'placeholder':'en hectare'}),
            'Type_occupation':forms.TextInput(attrs={'class':'form-control'})

        }

#demandeurs Moral

class DemandeursMoralForm(forms.ModelForm):
    class Meta:
        model = DemandeursMoral
        fields =['Nom_structure', 'date_de_creation', 'Nombre_adhérent', 
        'Adresse_physique', 'Quartier', 'Téléphone', 'Email', 'Superficie_demandée', 
        'Type_occupation'
        ]
        
        widgets ={
            'Nom_structure':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom de votre Structure'}),
            'date_de_creation':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Année-mois-Jour'}),
            'Nombre_adhérent':forms.TextInput(attrs={'class':'form-control'}),
            'Adresse_physique':forms.TextInput(attrs={'class':'form-control', 'placeholder':'adresse exacte  de votre Structure'}),
            'Quartier':forms.Select(attrs={'class':'form-control'}),
            'Téléphone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Votre numéro téléphone'}),
            'Email':forms.TextInput(attrs={'class':'form-control', 'placeholder':'email@example.com'}),
            'Superficie_demandée':forms.TextInput(attrs={'class':'form-control', 'placeholder':'en hectare'}),
            'Type_occupation':forms.TextInput(attrs={'class':'form-control'})

        }