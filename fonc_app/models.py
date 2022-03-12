from django.contrib import admin
from django.db import models

# demande pour les personnes physiques
class Demandeurs(models.Model ):
    STATUS =(('approuvée', 'approuvée'),('refusée', 'refusée'),('en attente', 'en attente'))
    SEXE =(('Masculin', 'Masculin'), ('Feminin', 'Feminin'))
    Quartier =(('HLM', 'HLM'), ('LEBOU EST', 'LEBOU EST'),('LEBOU OUEST', 'LEBOU OUEST'),('MBAMBARA', 'MBAMBARA'), ('NDIOB', 'NDIOB'), ('NGAYE DJITE', 'NGAYE DJITE'))
    Nom = models.CharField(max_length=25)
    Prénom = models.CharField(max_length=35)
    Profession = models.CharField(max_length=40)
    Date_de_naissance = models.DateField(max_length=8)
    Sexe = models.CharField(max_length=200, null=True, choices=SEXE)
    Nationalité = models.CharField(max_length=40)
    Adresse_physique= models.CharField(max_length=40)
    Quartier = models.CharField(max_length=200, null=True, choices=Quartier)
    Téléphone = models.IntegerField()
    Email = models.EmailField(max_length=40) 
    Superficie_demandée = models.IntegerField()
    Type_occupation = models.CharField(max_length=40)
    photo = models.ImageField(upload_to='media/photos', null=True)
    date_demande = models.DateTimeField(auto_now_add=True, null=True)
    statut =models.CharField(max_length=200, null=True, choices=STATUS)
    
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_demande']
    

class DemandeursAdmin(admin.ModelAdmin):
    list_display = ('Nom', 'Prénom', 'Profession', 'Date_de_naissance', 
    'Sexe', 'Nationalité', 'Adresse_physique', 'Quartier', 'Téléphone', 'Email',
    'Superficie_demandée', 'Type_occupation', 'photo', 'date_demande', 
    'statut')
    list_filter = ('Nom', )
    search_fields = ['Nom', 'Profession']

#demande pour personne morale
class DemandeursMoral(models.Model ):
    STATUS =(('approuvée', 'approuvée'),('refusée', 'refusée'),('en attente', 'en attente'),)
    Quartier =(('HLM', 'HLM'), ('LEBOU EST', 'LEBOU EST'),('LEBOU OUEST', 'LEBOU OUEST'),('MBAMBARA', 'MBAMBARA'), ('NDIOB', 'NDIOB'), ('NGAYE DJITE', 'NGAYE DJITE'))
    Nom_structure = models.CharField(max_length=25)
    date_de_creation = models.DateField()
    Nombre_adhérent = models.IntegerField()
    Adresse_physique= models.CharField(max_length=40)
    Quartier =models.CharField(max_length=200, null=True, choices=Quartier)
    Téléphone = models.IntegerField()
    Email = models.EmailField(max_length=40) 
    Superficie_demandée = models.IntegerField()
    Type_occupation = models.CharField(max_length=40)
    date_demande = models.DateTimeField(auto_now_add=True, null=True)
    statut =models.CharField(max_length=200, null=True, choices=STATUS)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_demande']
    

class DemandeursMoralAdmin(admin.ModelAdmin): 
    list_display =('Nom_structure', 'date_de_creation', 'Nombre_adhérent',
       'Adresse_physique', 'Téléphone', 'Email', 'Superficie_demandée', 
      'Type_occupation', 'date_demande')
    list_filter = ('Nom_structure', )
    search_fields = ['Nom_structure']

