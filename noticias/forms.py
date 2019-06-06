from django import forms
from .models import Noticia

class NoticiaForm(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ['titulo','subtitulo','cuerpo','imagen','url_noticia']
        widgets = {
            'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'subtitulo':forms.TextInput(attrs={'class':'form-control'}),
            'cuerpo':forms.Textarea(attrs={'class':'form-control'}),
            'url_noticia':forms.URLInput(attrs={'class':'form-control'})
        }
        labels = {
            'titulo':'Título' ,
            'subtitulo':'Subtítulo',
            'cuerpo':'Cuerpo de la noticia',
            'imagen':'Imagen',
            'url_noticia':'Fuente original',
        }