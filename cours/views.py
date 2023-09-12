from typing import Any, Dict
from django.db import models
from django.http import HttpResponseRedirect, FileResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from cours.forms import lessonForm, FormDeCommentaire, FormDeReponse
from cours.models import Niveaux, Matiere, Lesson
from django.views.generic import  DetailView, ListView, CreateView, UpdateView, DeleteView, FormView
# Create your views here.

def editeur_de_code(request):
    return render(request, 'editors/code.html')

class NiveauListView(ListView):
    context_object_name = 'niveaux'
    model = Niveaux
    template_name = 'programmes/niveaulist.html'

class MatiereListView(DetailView):
    context_object_name = 'niveau'
    model = Niveaux
    template_name = 'programmes/matierelist.html'

class LeconListView(ListView):
    paginate_by = 2
    context_object_name = 'matieres'
    model = Lesson
    template_name = 'programmes/leconlist.html'
    
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     nom = self.request.GET.get("recherche")
    #     if nom:
    #         queryset = queryset.filter(nom)
    #     return queryset


class LeconDetailView(DetailView, FormView):
    context_object_name = 'lecon'
    model = Lesson
    template_name = 'programmes/lecon_detail.html'
    form_class = FormDeCommentaire
    second_form_class = FormDeReponse

    def get_context_data(self, **kwargs):
        context = super(LeconDetailView, self).get_context_data(**kwargs)

        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()

        return context

    def form_valid(self, form):
        self.object = self.get_object()
        fd = form.save(commit=False)
        fd.auteur = self.request.user
        fd.nom_lecon_id = self.object.id
        fd.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form_valid2(self, form):
        self.object = self.get_object()
        fd = form.save(commit=False)
        fd.auteur = self.request.user
        fd.nom_comment_id = self.request.POST.get('comment_id')
        fd.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        self.object = self.get_object()
        niveau = self.object.niveau
        matiere = self.object.matiere
        return reverse_lazy('programme:lecondetail', kwargs={
            'niveau':niveau.slug,
            'matiere':matiere.slug, 
            'slug':self.object.slug
        })

    

    def post (self, request, *args, **kwargs):

        self.object = self.get_object()
        if 'form' in request.POST:
            form_class = self.form_class
            form_name = 'form'
        else:
            form_class = self.second_form_class
            form_name = 'form2'
        form = self.get_form(form_class)

        if form_name=='form' and form.is_valid():
            print("Nouveau commentaire")
            return self.form_valid(form)
        
        if form_name=='form2' and form.is_valid():
            print("Nouveau reponse")
            return self.form_valid2(form) 

def pdf_view(request, pk):
    # Récupérez le modèle qui contient le champ PDF, en utilisant la clé primaire (pk) ou un autre identifiant
    objet_pdf = Lesson.objects.get(pk=pk)
    
    # Récupérez le contenu du fichier PDF
    contenu_pdf = objet_pdf.pdf.read()  # Remplacez "votre_champ_pdf" par le nom de votre champ PDF

    # Créez une réponse de fichier pour renvoyer le PDF au navigateur
    response = FileResponse(contenu_pdf, content_type='application/pdf')
    
    return response


class leconCreateView(CreateView):
    form_class = lessonForm  # Spécifie le formulaire à utiliser pour la création de la leçon
    context_object_name = 'matieres'  # Le nom de l'objet contextuel à utiliser dans le template
    model = Matiere  # Le modèle associé à la vue
    template_name = 'programmes/lecon_create.html'  # Le chemin vers le template HTML

    # Cette méthode définit l'URL de redirection après la création réussie d'une leçon
    def get_success_url(self):
        self.object = self.get_object()
        niveau = self.object.niveau
        return reverse_lazy('cours:lecon', kwargs={'niveau': niveau.slug, 'slug': self.object.slug})

    # Cette méthode est appelée lorsque le formulaire est valide
    def form_valid(self, form):
        self.object = self.get_object()
        auto_identifier = form.save(commit=False)  # Crée une instance de Lecon sans l'enregistrer dans la base de données
        auto_identifier.auteur = self.request.user  # Définit l'auteur de la leçon comme l'utilisateur connecté
        auto_identifier.niveau = self.object.niveau  # Associe le niveau de la leçon au niveau de la matière
        auto_identifier.matiere = self.object  # Associe la matière à la leçon
        auto_identifier.save()  # Enregistre la leçon dans la base de données
        return HttpResponseRedirect(self.get_success_url())  # Redirige vers l'URL de succès
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Vous devez obtenir les instances de matiere et lecon ici et les ajouter au contexte
        context['matieres'] = Matiere # Obtenez l'instance de Matiere
        context['niveau'] = Niveaux # Obtenez l'instance de Niveaux
        return context


# modificaton de leçon

class LeconUpdateView(UpdateView):
    fields = ('nom', 'position', 'fpe', 'pdf',)  # Les champs du modèle Lecon que l'utilisateur peut mettre à jour
    context_object_name = 'lecon'  # Le nom de l'objet contextuel à utiliser dans le template
    model = Lesson  # Le modèle associé à la vue
    template_name = 'programmes/update_lecon.html'  # Le chemin vers le template HTML

# Suppression de leçon
class LeconDeleteView(DeleteView):
    model = Lesson  # Le modèle associé à la vue
    context_object_name = "lecon"  # Le nom de l'objet contextuel à utiliser dans le template
    template_name = "programmes/supprimer_lecon.html"  # Le chemin vers le template HTML

    # Cette méthode définit l'URL de redirection après la suppression réussie d'une leçon
    def get_success_url(self):
        niveau = self.object.niveau
        return reverse_lazy('cours:lecon', kwargs={'niveau': niveau.slug, 'slug': self.object.matiere.slug})


        
 