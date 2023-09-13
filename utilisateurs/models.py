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
    date_de_naissance = models.DateField(null=True, editable=True)
    pays = models.CharField(max_length=100, null=True, blank=True)
    ville =models.CharField(max_length=100, null=True, blank=True) 
    telephone = models.CharField(max_length=20, null=True, blank=True)
    photo = models.ImageField(upload_to=renommer_image, blank=True)
    select ='Non sexe'
    FEMININ = 'F'
    MASCULIN = 'M'
    SEXE = [
        (select, 'Selectionner sexe'),
        (FEMININ, 'feminnin'),
        (MASCULIN, 'masculin')
    ]
    sexe = models.CharField(max_length=8, choices=SEXE, default=select)

    APPRENANT = 'Apprenant(e)'
    ETUDIANT = 'Etudiant(e)'
    ENSEIGNANT = 'Enseignant(e)'
    TYPES = [
        (APPRENANT, 'Apprenant(e)'),
        (ETUDIANT, 'Etudiant(e)'),
        (ENSEIGNANT, 'Enseignant(e)')
    ]

    type_user = models.CharField(max_length=14, choices=TYPES, default=ETUDIANT)

    def __str__ (self):
        return self.user.username
    
    # def update_profile(self, data):
    #     self.date_de_naissance = data.get('date_de_naissance', self.date_de_naissance)
    #     self.pays = data.get('pays', self.pays)
    #     self.ville = data.get('ville', self.ville)
    #     self.telephone = data.get('telephone', self.telephone)
    #     self.photo = data.get('photo', self.photo)
    #     self.sexe = data.get('sexe', self.sexe)
    #     self.type_user = data.get('type_user', self.type_user)
    #     self.save()

class Code(models.Model):
    code_html = models.TextField(max_length=800, blank=True)
    code_css = models.TextField(max_length=800, blank=True)
    code_js = models.TextField(max_length=800, blank=True)


