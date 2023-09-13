from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Niveaux(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.nom
    
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.nom)
    #     super().save(*args, **kwargs)

class Matiere (models.Model):
    matiere_id = models.CharField(unique=True, max_length=100)
    nom = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    niveau = models.ForeignKey(Niveaux, on_delete=models.CASCADE, related_name='matieres')
    image = models.ImageField(upload_to='matieres', blank=True)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.nom
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

class Lesson(models.Model):
    lesson_id = models.CharField(unique=True, max_length=100, verbose_name="Identifiant de leçon")
    niveau = models.ForeignKey(Niveaux, on_delete=models.CASCADE)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name='lecon') 
    titre = models.CharField(max_length=100, verbose_name="Titre de leçon")
    slug = models.SlugField(blank=True, null=True)
    video = models.FileField(upload_to="VIDEOS", null=True, blank=True, verbose_name='Video de cours')
    pdf = models.FileField(upload_to="PDF", null=True, blank=True, verbose_name='pdf de cours')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def get_pdf_url(self):
        return reverse('cours:lesson', kwargs={'niveau':self.niveau.slug, 'slug':self.matiere.slug})
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.titre
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("cours:lecon", kwargs={"niveau": self.niveau.slug, 'slug':self.matiere.slug})
    

class Commentaire(models.Model):
    nom_lecon = models.ForeignKey(Lesson, null=True, on_delete=models.CASCADE, related_name="comment_lecon")
    nom_comment = models.CharField(max_length=100, blank=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)

    # je modifier la colonne "nom_comment"
    def save(self, *args, **kwargs):
        self.nom_comment = slugify('commenter par ' + str(self.auteur) + " à " + str(self.created_at))
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nom_comment
    # ordonner les commentaire par la dat de creation le plus recent
    class Meta():
        ordering = ['-created_at']

class Reponse(models.Model):
    nom_comment = models.ForeignKey(Commentaire, on_delete=models.CASCADE, related_name="reponse_comment")
    contenu = models.TextField(max_length=600)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "reponse a " + str(self.nom_comment.nom_comment)
