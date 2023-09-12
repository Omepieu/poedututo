from django.contrib import admin
from cours.models import *

# Register your models here.
class NiveauAdmin(admin.ModelAdmin):
    list_display = ('nom', 'slug', 'description')

admin.site.register(Niveaux)

class MatiereAdmin(admin.ModelAdmin):
    list_display = ('matiere_id', 'nom', 'niveau')

admin.site.register(Matiere)

class lessonAdmin(admin.ModelAdmin):
    list_display = ('lesson_id', 'niveau', 'auteur', 'matiere', 'titre', 'pdf', 'created')
    
admin.site.register(Lesson)

