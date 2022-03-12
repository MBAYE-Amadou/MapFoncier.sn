from django.db.models import query
from django.shortcuts import redirect, render
from fonc_app.models import Demandeurs, DemandeursMoral
from .formulaire import DemandeursForm
from .formulaire import DemandeursMoralForm
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import get_template
import pdfkit
import io

# Create your views here.
def demande_view(request):
    if request.method == 'POST':   
        form = DemandeursForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        messages.success(request, "Votre demande est enregistrée avec Succés !")
        return redirect('/verification')
    else:
        form = DemandeursForm()
    return render(request, 'formdemande.html', {'form':form })

def home_view(request):
    return render(request, 'home.html')

def contact_view(request):
    if request.method =="POST":
        subject = request.POST.get('subject', '')
        message_name =request.POST.get('message-name')
        message_email =request.POST['message-email']
        message =request.POST['message']

        #send email
        message ='''
        Nouveau message: {}
        
        From : {}
        '''.format( message, message_email)


        send_mail(
            subject, 
            message,
            message_email,          
            ['mbayeamadouugb@gmail.com'],
        fail_silently=False)
        return render(request, 'contact.html',{'message_name': message_name})
    else:
        return render(request, 'contact.html',{})

def info_view(request):
    return render(request, 'infos_demande.html')

def about_view(request):
    return render(request, 'about.html')

#form personne morale
def demandebis_view(request):
    if request.method == 'POST':   
        form = DemandeursMoralForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        messages.success(request, "Votre demande est enregistrée avec Succés !")
        return redirect('/verifications')
    else:
        form = DemandeursMoralForm()
    return render(request, 'formdemandebis.html', {'form':form })

#Bar de Recherche
def searchBar_view(request):
    if request.method =='GET':
        query = request.GET.get('query')
        if query:
            adresses = Demandeurs.objects.filter(Adresse_physique__icontains = query)
            return render(request, 'search.html', {'adresses': adresses})
        else:
            print("Votre recherche n'a pas donné de résultat.")
            return request(request, 'search.html', {})

# pdf et telechargement du formulaire
# pour les personnes physiques
def show_demandeurs(request):
    data = Demandeurs.objects.all()[:1]
    for dem in data:
        Nom = dem.Nom
        Prénom = dem.Prénom
        Profession = dem.Profession
        Date_de_naissance = dem.Date_de_naissance
        Sexe = dem.Sexe
        Nationalité = dem.Nationalité
        Adresse_physique = dem.Adresse_physique
        Quartier = dem.Quartier
        Téléphone = dem.Téléphone
        Email = dem.Email
        Superficie_demandée  = dem.Superficie_demandée 
        Type_occupation = dem.Type_occupation
        date_demande = dem.date_demande
    
    return render(request, 'showinfodemande.html', {'Nom':Nom, 'Prénom':Prénom, 'Profession':Profession, 
                                                    'Date_de_naissance':Date_de_naissance, 'Sexe':Sexe,
                                                    'Nationalité':Nationalité, 'Adresse_physique':Adresse_physique, 'Quartier':Quartier,
                                                    'Téléphone':Téléphone, 'Email':Email, 'Superficie_demandée':Superficie_demandée,
                                                    'Type_occupation':Type_occupation, 'date_demande':date_demande})

# fonction pour generer  le formulaire personne physique en pdf
def generer(request, id):
    demandeurs = Demandeurs.objects.get(pk=id)
    Nom = demandeurs.Nom
    Prénom = demandeurs.Prénom
    Profession = demandeurs.Profession
    Date_de_naissance = demandeurs.Date_de_naissance
    Sexe = demandeurs.Sexe
    Nationalité = demandeurs.Nationalité
    Adresse_physique = demandeurs.Adresse_physique
    Quartier = demandeurs.Quartier
    Téléphone = demandeurs.Téléphone
    Email = demandeurs.Email
    Superficie_demandée  = demandeurs.Superficie_demandée 
    Type_occupation = demandeurs.Type_occupation
    date_demande = demandeurs.date_demande
    num = id
    
    template = get_template('generateur.html')
    context ={'Nom':Nom.upper(), 'Prénom':Prénom.upper(), 'Profession':Profession, 
                                                    'Date_de_naissance':Date_de_naissance, 'Sexe':Sexe, 'num':num,
                                                    'Nationalité':Nationalité, 'Adresse_physique':Adresse_physique, 'Quartier':Quartier,
                                                    'Téléphone':Téléphone, 'Email':Email, 'Superficie_demandée':Superficie_demandée,
                                                    'Type_occupation':Type_occupation, 'date_demande':date_demande}
    html = template.render(context)
    options = {
        'page-size':'Letter',
        'encoding':'UTF-8',
    }
    pdf = pdfkit.from_string(html, False, options)
    
    reponse = HttpResponse(pdf, content_type='fonc_app')
    reponse['Content-Disposition']='filename="formulaire.pdf"'
    return reponse

#Création fonction pour telecharger le form
def download(request):
    demandeurs = Demandeurs.objects.all()[:1]
    return render(request, 'download.html', {'demandeurs':demandeurs}) 


# pdf et telechargement du formulaire
# pour les personnes morales
def show_demandeursbis(request):
    data = DemandeursMoral.objects.all()[:1]
    for dem in data:
        Nom_structure = dem.Nom_structure
        date_de_creation = dem.date_de_creation
        Nombre_adhérent = dem.Nombre_adhérent
        Adresse_physique = dem.Adresse_physique
        Quartier = dem.Quartier
        Téléphone  = dem.Téléphone
        Email = dem.Email
        Superficie_demandée  = dem.Superficie_demandée 
        Type_occupation = dem.Type_occupation
        date_demande = dem.date_demande
    
    return render(request, 'showinfodemandebis.html', {'Nom_structure':Nom_structure, 'date_de_creation':date_de_creation, 'Nombre_adhérent':Nombre_adhérent, 
                                                    'Adresse_physique':Adresse_physique, 'Quartier':Quartier, 'Téléphone':Téléphone, 'Email':Email, 
                                                    'Superficie_demandée':Superficie_demandée, 'Type_occupation':Type_occupation, 'date_demande':date_demande})
    

# fonction pour generer  le formulaire personnes Morales en pdf
def generer_bis(request, id):
    societes = DemandeursMoral.objects.get(pk=id)
    Nom_structure = societes.Nom_structure
    date_de_creation = societes.date_de_creation
    Nombre_adhérent = societes.Nombre_adhérent
    Adresse_physique = societes.Adresse_physique
    Quartier = societes.Quartier
    Téléphone  = societes.Téléphone
    Email = societes.Email
    Superficie_demandée  = societes.Superficie_demandée 
    Type_occupation = societes.Type_occupation
    date_demande = societes.date_demande
    num = id
    
    template = get_template('generateur_bis.html')
    context ={'Nom_structure':Nom_structure, 'date_de_creation':date_de_creation, 'Nombre_adhérent':Nombre_adhérent, 'num':num,
                                                    'Adresse_physique':Adresse_physique, 'Quartier':Quartier, 'Téléphone':Téléphone, 'Email':Email, 
                                                    'Superficie_demandée':Superficie_demandée, 'Type_occupation':Type_occupation, 'date_demande':date_demande}
    html = template.render(context)
    options = {
        'page-size':'Letter',
        'encoding':'UTF-8',
    }
    pdf = pdfkit.from_string(html, False, options)
    
    reponse = HttpResponse(pdf, content_type='fonc_app')
    reponse['Content-Disposition']='filename="formulaire.pdf"'
    return reponse

#Fonction pour telecharger le form
def telecharger(request):
    societes = DemandeursMoral.objects.all()[:1]
    return render(request, 'download_bis.html', {'societes':societes}) 
