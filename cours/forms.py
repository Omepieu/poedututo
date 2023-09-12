from django import forms
from cours.models import Lesson, Commentaire, Reponse


class lessonForm(forms.ModelForm):
    class Meta():
        model = Lesson
        fields = ('lesson_id','titre', 'slug', 'video', 'pdf')

        # widgets = {
        #     'lecon_id': forms.TextInput(attrs={'class':'form-control'}),
        #     'nom': forms.TextInput(attrs={'class':'form-control'}),
        #     'slug': forms.TextInput(attrs={'class':'form-control'}),
        #     'position': forms.NumberInput(attrs={'class':'form-control'}),
        #     'video': forms.FileInput(attrs={'class':'form-control'}),
        #     'fpe': forms.TextInput(attrs={'class':'form-control'}),
        #     'pdf': forms.FileInput(attrs={'class':'form-control'}),
        #     'content':forms.Textarea(attrs={'class':'form-control'}),
            
        # }

class FormDeCommentaire(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ('contenu',)
        lables = {'contenu':'Commenter'}
        widgets ={
            'contenu': forms.TextInput(attrs={
                'class':'form-control',
                'rows':4,
                'cols':70,
                'placeholder':'Redigez un commantaire'
            })
        }

class FormDeReponse(forms.ModelForm):
    class Meta:
        model = Reponse
        fields = ('contenu',)
        lables = {'contenu':'Commenter'}
        widgets ={
            'contenu':forms.TextInput(attrs={
                'class':'form-control',
                'rows':4,
                'cols':40,
                'placeholder':'Redigez une reponse'
            })
        }
