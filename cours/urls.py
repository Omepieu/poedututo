from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cours.views import *

app_name = "cours"
urlpatterns = [
    path('', NiveauListView.as_view(), name='niveau_liste'),
    path('/editeur', editeur_de_code, name='editeur'),
    path('<slug:slug>/', MatiereListView.as_view(), name='matiere'),
    path('<str:niveau>/<slug:slug>', LeconListView.as_view(), name='lesson'),
    path('<str:niveau>/<slug:slug>/creer', leconCreateView.as_view(), name='leconcreate'),
    path('<str:niveau>/<slug:matiere>/<slug:slug>', LeconDetailView.as_view(), name='lecondetail'),
    path('<str:niveau>/<slug:matiere>/<slug:slug>/modifier', LeconUpdateView.as_view(), name='lecon_modifier'),
    path('<str:niveau>/<slug:matiere>/<slug:slug>/supprimer', LeconDeleteView.as_view(), name='lecon_supprimer'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)