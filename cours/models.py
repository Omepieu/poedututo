from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone



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
    video = models.FileField(blank=True, null=True, upload_to="VIDEO")
    content = RichTextUploadingField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_pdf_url(self):
        return reverse('cours:lesson', kwargs={'niveau':self.niveau.slug, 'slug':self.matiere.slug})
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.titre
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super(Lesson, self).save(*args, **kwargs)

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

class Code(models.Model):
    code_html = models.TextField(max_length=800, blank=True)
    code_css = models.TextField(max_length=800, blank=True)
    code_js = models.TextField(max_length=800, blank=True)


class Question(models.Model):
    question_id = models.CharField(unique=True, max_length=100, verbose_name="Identifiant de question", null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='questions')
    texte_question = models.TextField(verbose_name="Texte de la question", null=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE,default=None, null=True)
    created = models.DateTimeField(auto_now_add=False, default=timezone.now)
    updated = models.DateTimeField(auto_now=False, default=timezone.now)

    def __str__(self):
        return self.texte_question

class Anwser(models.Model):
    reponse_id = models.CharField(unique=True, max_length=100, verbose_name="Identifiant de réponse", null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='reponses')
    texte_reponse = models.TextField(verbose_name="Texte de la réponse", null=True)
    EST_CORRECTE_CHOIX = (
        ('radio', 'Radio'),
        ('checkbox', 'Checkbox'),
        ('text', 'Text'),
    )
    type_input = models.CharField(max_length=10, choices=EST_CORRECTE_CHOIX, default='radio', verbose_name="Type d'input")
    est_correcte = models.BooleanField(default=False, verbose_name="Est correcte")
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    created = models.DateTimeField(auto_now_add=False, default=timezone.now)
    updated = models.DateTimeField(auto_now=False, default=timezone.now)

    def __str__(self):
        return self.texte_reponse
