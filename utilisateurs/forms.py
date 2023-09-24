from django import forms
from utilisateurs.models import Profil
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'last_name',
            'email',
            'password1',
            'password2'
        ]
        widgets = {
            'username':forms.TextInput(attrs={'class': 'form-control'}),
            'first_name':forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.TextInput(attrs={'class': 'form-control'}),
            'password1':forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2':forms.PasswordInput(attrs={'class': 'form-control'})
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'username', 'last_name', 'email']

class ProfilUpdateForm(forms.ModelForm):
    class Meta():
        model = Profil
        fields = ['date_de_naissance', 'pays', 'ville', 'telephone', 'sexe', 'type_user', 'photo']
        widgets = {
            'date_de_naissance':forms.DateInput(attrs={'class': 'form-control'}),
            'pays':forms.TextInput(attrs={'class': 'form-control'}),
            'ville':forms.TextInput(attrs={'class': 'form-control'}),
            'telephone':forms.TextInput(attrs={'class': 'form-control'}),
            'sexe':forms.Select(attrs={'class': 'form-control'}),
            'type_user':forms.Select(attrs={'class': 'form-control'}),
            'photo':forms.FileInput(attrs={'class': 'form-control'}),
        }


