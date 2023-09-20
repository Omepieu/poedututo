from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cours.views import *

app_name = "cours"
urlpatterns = [
    
    path('', accueil, name='accueil'),
    path('courses/', NiveauListView.as_view(), name='niveau_liste'),
    path('courses/editeur/', editeur_de_code, name='editeur'),
    path('courses/<slug:slug>/', MatiereListView.as_view(), name='matiere'),
    path('courses/<str:niveau>/<slug:slug>', LeconListView.as_view(), name='lesson'),
    path('courses/<str:niveau>/<slug:slug>/creer', leconCreateView.as_view(), name='leconcreate'),
    path('courses/<str:niveau>/<slug:matiere>/<slug:slug>', LeconDetailView.as_view(), name='lecondetail'),
    path('courses/<str:niveau>/<slug:matiere>/<slug:slug>/modifier', LeconUpdateView.as_view(), name='lecon_modifier'),
    path('courses/<str:niveau>/<slug:matiere>/<slug:slug>/supprimer', LeconDeleteView.as_view(), name='lecon_supprimer'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)