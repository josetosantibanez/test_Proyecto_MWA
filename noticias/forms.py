from django import forms
from .models import Noticia

class NoticiaForm(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ['titulo','subtitulo','cuerpo','imagen','url_noticia']
        widgets = {
            'titulo':forms.TextInput(attrs={'class':'form-control mb-3'}),
            'subtitulo':forms.TextInput(attrs={'class':'form-control mb-3'}),
            'cuerpo':forms.Textarea(attrs={'class':'form-control mb-3'}),
            'url_noticia':forms.URLInput(attrs={'class':'form-control mb-3'})
        }
        labels = {
            'titulo':'Título' ,
            'subtitulo':'Subtítulo',
            'cuerpo':'Cuerpo de la noticia',
            'imagen':'Imagen',
            'url_noticia':'Fuente original',
        }