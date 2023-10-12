from django.contrib import admin
from utilisateurs.models import Profil

# Register your models here.

class ProfilAdmin(admin.ModelAdmin):
    list_display = ('date_de_naissance', 'pays', 'ville', 'telephone', 'sexe', 'type_user')

admin.site.register(Profil, ProfilAdmin)  # Register the Profil model with its admin class

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')

admin.site.site_title ="Admin SCHOOL ON LINE"
admin.site.site_header ="SCHOOL ON LINE"
admin.site.index_title ="Administrateur"


