from django import forms
from cours.models import Lesson, Commentaire, Reponse, Code


class lessonForm(forms.ModelForm):
    class Meta():
        model = Lesson
        fields = ('lesson_id','titre','niveau', 'matiere', 'content')

        widgets = {
        #     'lecon_id': forms.TextInput(attrs={'class':'form-control'}),
        #     'nom': forms.TextInput(attrs={'class':'form-control'}),
        #     'slug': forms.TextInput(attrs={'class':'form-control'}),
        #     'position': forms.NumberInput(attrs={'class':'form-control'}),
        #     'video': forms.FileInput(attrs={'class':'form-control'}),
        #     'fpe': forms.TextInput(attrs={'class':'form-control'}),
        #     'pdf': forms.FileInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control', 'id':'editor'}),
            
         }

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
        
class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = [
            'code_html', 
            'code_css', 
            'code_js',
        ]
        widgets = {
            'code_html':forms.Textarea(attrs={'class': 'texetarea', 'id':'html-code'}),
            'code_css':forms.Textarea(attrs={'class': 'texetarea', 'id':'css-code'}),
            'code_js':forms.Textarea(attrs={'class': 'texetarea', 'id':'js-code'}),
        }
