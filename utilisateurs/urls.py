from django.urls import path
from utilisateurs import views
from django.conf import settings
from django.conf.urls.static import static
from utilisateurs import views
APP_NAME = 'utilisateurs'
urlpatterns = [
    path('registeur', views.registeur, name='registeur'),
    path('connexion', views.connexion, name='connexion'),
    path('logout', views.deconnection, name='logout'),
    path('profil', views.update_profile, name='profil'),
    path('liste_users', views.recupere_users, name='liste_users'),

    path('code', views.sauvegader, name='code'),

    # path("dashboard", bord, name="dashboard"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)