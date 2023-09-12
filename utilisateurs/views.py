from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from utilisateurs.forms import UserForm,CodeForm, UserUpdateForm, ProfilUpdateForm
from utilisateurs.models import Profil
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
# def bord(request):
#     return render(request, 'utilisateurs/bord.html')

def accueil(request):
    return render(request, 'base/home.html')


def registeur(request):
    registeur_id = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid:
            user_form.save()
            registeur_id = True
            return HttpResponseRedirect('connexion')
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    context = {'form1':user_form, 'registeur_id':registeur_id}
    return render(request, 'utilisateur/registeur.html', context)

def connexion(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user :
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
               return render(request, 'utilisateurs/inactive.html')
        else:
            return render(request, 'utilisateur/connexion.html', {'message': "Veuillez compléter correctement les champs « nom d’utilisateur » et « mot de passe » d'un compte autorisé"})
    else:
        return render(request, 'utilisateur/connexion.html')
    
    
@login_required
def deconnection(request):
    logout (request)
    return HttpResponseRedirect('/')


def sauvegader(request):
    if request.method == "POST":
        form = CodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('code')
    else:
        form = CodeForm(request.POST)

    return render(request, 'base/source.html', {'form':form})

@login_required
def update_profile(request):
    user = request.user  # L'utilisateur connecté
    #profil = Profil.objects.get(user=user) # Le profil associé à l'utilisateur
     # Essayez de récupérer le modèle Profil associé à l'utilisateur, s'il existe
    try:
        profil = Profil.objects.get(user=user)

    # Si le modèle Profil n'existe pas encore, créez-le
    except Profil.DoesNotExist:
        profil = Profil(user=user)
        
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user)
        profil_form = ProfilUpdateForm(request.POST, request.FILES, instance=profil)

        if user_form.is_valid() and profil_form.is_valid():
            user_form.save()  # Met à jour les informations de l'utilisateur
            profil_form.save()  # Met à jour les informations du profil
            messages.success(request, 'Profil mis à jour avec succès.')
            return redirect('accueil')  # Redirigez l'utilisateur vers sa page de profil après la mise à jour

    else:
        user_form = UserUpdateForm(instance=user)
        profil_form = ProfilUpdateForm(instance=profil)

    context = {'user_form': user_form, 'profil_form': profil_form}
    return render(request, 'utilisateur/profil.html', context) 

def recupere_users(request):
    users = User.objects.all()
    profils = Profil.objects.all()
    context = {'users':users, 'profils':profils}
    return render(request, 'utilisateur/list_user.html', context)