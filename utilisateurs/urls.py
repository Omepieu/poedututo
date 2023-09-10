from django.urls import path
from utilisateurs import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('registeur', views.registeur, name='registeur'),
    path('code', views.sauvegader, name='code'),

    # path('connexion', connecter, name='connexion'),
    # path('logout', sedeconnecter, name='logout'),
    # path("dashboard", bord, name="dashboard"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)