from django import forms
from utilisateurs.models import Profil, Code
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
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
            'password1':forms.TextInput(attrs={'class': 'rounded-md'}),
            'password2':forms.TextInput(attrs={'class': 'rounded-md'})
        }

class ProfileForm(forms.ModelForm):
    class Meta():
        model = Profil
        fields = [
            'date_de_naissance',
            'pays',
            'ville', 
            'telephone', 
            'sexe',
            'type_user',
            'photo'
        ]
        widgets  = {
            'date_de_naissance':forms.DateInput(attrs={'class': 'form-control'}),
            'pays':forms.TextInput(attrs={'class': 'form-control'}),
            'ville':forms.TextInput(attrs={'class': 'form-control'}),
            'telephone':forms.TextInput(attrs={'class': 'form-control'}),
            'sexe':forms.Select(attrs={'class': 'form-control'}),
            'types':forms.Select(attrs={'class': 'form-control'}),
            'photo':forms.FileInput(attrs={'class': 'form-control'}),

        }

class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = [
            'code_html', 
            'code_css', 
            'code_js',
        ]
        widgets = {
            'code_html':forms.Textarea(attrs={'class': 'test', 'id':'html-code'}),
            'code_css':forms.Textarea(attrs={'class': 'test', 'id':'css-code'}),
            'code_js':forms.Textarea(attrs={'class': 'test', 'id':'js-code'}),
        }
