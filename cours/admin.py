from django.contrib import admin
from cours.models import *

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
    list_display = ('lesson_id', 'niveau', 'auteur', 'matiere', 'titre', 'pdf', 'created')
    ordering = ['id']
    search_fields = ('titre',)
    
admin.site.register(Lesson, lessonAdmin)

class CodeAdmin(admin.ModelAdmin):
    list_display = ('code_html', 'code_css', 'code_js')

admin.site.register(Code, CodeAdmin)  # Register the Code model with its admin class
