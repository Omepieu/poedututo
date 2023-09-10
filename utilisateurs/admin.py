from django.contrib import admin
from utilisateurs.models import Profil, Code


# Register your models here.

class ProfilAdmin(admin.ModelAdmin):
    list_display = ('date_de_naissance', 'pays', 'ville', 'telephone', 'sexe','type_user')

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')

class CodeAdmin(admin.ModelAdmin):
    list_display = ('code_html', 'code_css', 'code_js')

admin.site.register(Profil, ProfilAdmin)
admin.site.register(Code, CodeAdmin)
