from django.shortcuts import redirect, render
from utilisateurs.forms import UserForm, ProfileForm, CodeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
# def bord(request):
#     return render(request, 'utilisateurs/bord.html')

def accueil(request):
    return render(request, 'main.html')


def registeur(request):
    registeur_id = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        if user_form.is_valid and profile_form.is_valid():
            user = user_form.save()
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registeur_id = True
            return HttpResponseRedirect('')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    context = {'form1':user_form, 'form2':profile_form, 'registeur_id':registeur_id}
    return render(request, 'utilisateur/registeur.html', context)

# def connecter(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user :
#             if user.is_active:
#                 login(request, user)
#                 return redirect('/')
#             else:
#                return render(request, 'utilisateurs/inactive.html')
#         else:
#             return render(request, 'utilisateurs/login.html', {'message': "Nom d'utilisateur ou mot de passe incorrect"})
#     else:
#         return render(request, 'utilisateurs/login.html')
    
# @login_required
# def sedeconnecter(request):
#     logout (request)
#     return HttpResponseRedirect('/')


def sauvegader(request):
    if request.method == "POST":
        form = CodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('code')
    else:
        form = CodeForm(request.POST)

    return render(request, 'base/source.html', {'form':form})
    
