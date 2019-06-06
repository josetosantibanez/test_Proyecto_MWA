from django import forms
from .models import Miembro

class MiembroForm(forms.ModelForm):

    class Meta:
        model = Miembro
        fields = ['rut','nombres','apellido_p','apellido_m','fecha_nacimiento',
        'correo','celular','direccion','genero']
        widgets = {
            'rut':forms.TextInput(attrs={'class':'form-control-lg mb-2'}),
            'nombres':forms.TextInput(attrs={'class':'form-control-lg mb-2'}),
            'apellido_p':forms.TextInput(attrs={'class':'form-control-lg mb-2'}),
            'apellido_m':forms.TextInput(attrs={'class':'form-control-lg mb-2'}),
            'fecha_nacimiento':forms.DateInput(attrs={'class':'form-control-lg mb-2'}),
            'correo':forms.TextInput(attrs={'class':'form-control-lg mb-2'}),
            'celular':forms.TextInput(attrs={'class':'form-control-lg mb-2'}),
            'direccion':forms.TextInput(attrs={'class':'form-control-lg mb-2'}),
            'genero':forms.TextInput(attrs={'class':'form-control-lg mb-2'}),
        }
        labels = {
            'rut':'Rut' ,
            'nombres':'Nombre',
            'apellido_p':'Apellido paterno',
            'apellido_m':'Apellido materno',
            'fecha_nacimiento':'Fecha de nacimiento',
            'correo':'Correo electronico',
            'celular':'Numero celular',
            'direccion':'Direccion',
            'genero':'Género',
        }
       
    