from fonc_app.formulaire import DemandeursForm
from fonc_app.models import Demandeurs
from fonc_app.models import DemandeursMoral
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
from .forms import DemandeurForm
from .forms import DemandeurMoralForm


# Mes vues ici.
#Login
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pwd = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=pwd)
            if user is not None:
                login(request, user)
                return redirect('admin_choice')
            else:
                messages.error(request, "Désolé ! Accés interdit")
                return render(request, 'login.html', {'form':form})
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'

            return render(request, 'login.html', {'form':form})

    else:
        form = LoginForm()
        return render(request, 'login.html', {'form':form})


def admindemande_view(request):
    dataDemandeur =Demandeurs.objects.all()
    context ={'dataDemandeur':dataDemandeur}
    return render(request, 'gesdemande.html', context)

def deletedemande_view(request, pk):
    demand =Demandeurs.objects.get(id=pk)
    if request.method=='POST':
        demand.delete()
        messages.success(request, "Suppréssion réussie !")
        return redirect('demande')
    context={'item':demand}
    return render(request,'supprimer_demande.html',context)


def updatedemande_view(request, pk):
    demand_update =Demandeurs.objects.get(id=pk)
    form =DemandeurForm(instance=demand_update)

    if request.method=='POST':
        form =DemandeurForm(request.POST, instance=demand_update)
        if form.is_valid():
            form.save()
            return redirect('demande')
    context={'form': form}
    return render(request,'update.html', context)

#Vue pour le choix de la demande
#à administrer
def infogestion_view(request):
    return render(request, 'infos_gesdemande.html')


#Administration demande personne morale
def admindemandebis_view(request):
    dataDemandeurmoral =DemandeursMoral.objects.all()
    context ={'dataDemandeurmoral':dataDemandeurmoral}
    return render(request, 'gesdemandebis.html', context)


def updatedemandebis_view(request, pk):
    demande_update =DemandeursMoral.objects.get(id=pk)
    form =DemandeurMoralForm(instance=demande_update)

    if request.method=='POST':
        form =DemandeurMoralForm(request.POST, instance=demande_update)
        if form.is_valid():
            form.save()
            return redirect('demandebis')
    context={'form':form}
    return render(request,'updatebis.html',context)


def deletedemandebis_view(request, pk):
    demand =DemandeursMoral.objects.get(id=pk)
    if request.method=='POST':
        demand.delete()
        messages.success(request, "Suppréssion réussie !")
        return redirect('demandebis')
    context={'item':demand}
    return render(request,'supprimer_demandebis.html',context)


