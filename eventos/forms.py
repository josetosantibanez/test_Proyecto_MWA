from django import forms
from .models import Evento, Asistentes

class EventoForm(forms.ModelForm):

    class Meta:
        model = Evento
        fields = ['nombre','cupos','fecha','ubicacion','descripcion','imagen']
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control mb-2'}),
            'cupos':forms.TextInput(attrs={'class':'form-control mb-2'}),
            'fecha':forms.DateTimeInput(attrs={'class':'form-control mb-2'}),
            'ubicacion':forms.TextInput(attrs={'class':'form-control mb-2'}),
            'descripcion':forms.DateInput(attrs={'class':'form-control mb-2'}),
            }
        labels = {
            'nombre':'Evento' ,
            'cupos':'Cupos disponibles',
            'fecha':'Fecha del evento',
            'ubicacion':'Dirección',
            'descripcion':'Descripción',
            'imagen':'Imagen',
        }

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistentes
        fields = ['miembro','evento']
        widgets = {
            'miembro':forms.HiddenInput(),
            'evento':forms.HiddenInput(),
            }
       
    