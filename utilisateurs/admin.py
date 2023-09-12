from django.contrib import admin
from utilisateurs.models import Profil, Code

# Register your models here.

class ProfilAdmin(admin.ModelAdmin):
    list_display = ('date_de_naissance', 'pays', 'ville', 'telephone', 'sexe', 'type_user')

admin.site.register(Profil, ProfilAdmin)  # Register the Profil model with its admin class

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')

class CodeAdmin(admin.ModelAdmin):
    list_display = ('code_html', 'code_css', 'code_js')

admin.site.register(Code, CodeAdmin)  # Register the Code model with its admin class

