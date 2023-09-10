from django.db import models
from django.contrib.auth.models import User
import os

# Crée une fonction pour renommer une image de profil
def renommer_image(instance, filename):
    upload_to = 'photos'
    extension = filename.split('.')[-1]
    if instance.user.username:
        filename = f'{instance.user.username}.{extension}'
    return os.path.join(upload_to, filename)

class Profil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_de_naissance = models.DateField(auto_now_add=False, null=True)
    pays = models.CharField(max_length=100, null=True, blank=True)
    ville =models.CharField(max_length=100, null=True, blank=True) 
    telephone = models.CharField(max_length=20, null=True, blank=True)
    photo = models.FileField(upload_to=renommer_image, blank=True)
    select ='Non sexe'
    FEMININ = 'F'
    MASCULIN = 'M'
    SEXE = [
        (select, 'Selectionner sexe'),
        (FEMININ, 'feminnin'),
        (MASCULIN, 'masculin')
    ]
    sexe = models.CharField(max_length=8, choices=SEXE, default=select)

    APPRENANT = 'appre'
    ETUDIANT = 'ETU'
    ENSEIGNANT = 'ENSEI'
    TYPES = [
        (APPRENANT, 'Apprenant(e)'),
        (ETUDIANT, 'Etudiant(e)'),
        (ENSEIGNANT, 'Enseignant(e)')
    ]

    type_user = models.CharField(max_length=9, choices=TYPES, default=ETUDIANT)

    def __str__ (self):
        return self.user.username

class Code(models.Model):
    code_html = models.TextField(max_length=800, blank=True)
    code_css = models.TextField(max_length=800, blank=True)
    code_js = models.TextField(max_length=800, blank=True)


