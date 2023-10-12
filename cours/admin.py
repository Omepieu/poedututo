from django.contrib import admin
from cours.models import *
from django import forms
from ckeditor.widgets import CKEditorWidget
# Register your models here.
class NiveauAdmin(admin.ModelAdmin):
    list_display = ('nom', 'slug', 'description')
    prepopulated_fields = {'slug': ('nom',)}
    ordering = ['id']

admin.site.register(Niveaux, NiveauAdmin)

class MatiereAdmin(admin.ModelAdmin):
    list_display = ('matiere_id', 'nom', 'niveau', 'image')
    ordering = ['id']

admin.site.register(Matiere, MatiereAdmin)

class lessonAdmin(admin.ModelAdmin):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Lesson
        fields = ('lesson_id', 'niveau', 'auteur', 'matiere', 'titre', 'content')

    list_display = ('lesson_id', 'niveau', 'auteur', 'matiere', 'titre', 'created')
    ordering = ['id']
    search_fields = ('titre',)
    
admin.site.register(Lesson, lessonAdmin)

class CodeAdmin(admin.ModelAdmin):
    list_display = ('code_html', 'code_css', 'code_js')

admin.site.register(Code, CodeAdmin)  # Register the Code model with its admin class


class QuestionAdmin(admin.ModelAdmin):
    list_display =('question_id', 'texte_question', 'lesson','auteur')
    ordering = ['id']
    search_fields = ('texte_question','lesson','auteur')

admin.site.register(Question, QuestionAdmin)

class AnwserAdmin(admin.ModelAdmin):
    list_display =('reponse_id', 'texte_reponse', 'question','auteur', 'est_correcte')
    ordering = ['id']
    search_fields = ('texte_reponse','question','auteur')

admin.site.register(Anwser, AnwserAdmin)