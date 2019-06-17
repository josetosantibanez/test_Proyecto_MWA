from django import forms
from .models import Miembro

class MiembroForm(forms.ModelForm):
    class Meta:
        
        model = Miembro

        GENERO_OPCIONES=[
            ('M','Masculino'),
            ('F','Femenino'),
        ]

        fields = ['rut','nombres','apellido_p','apellido_m','fecha_nacimiento',
        'correo','celular','direccion','genero']
        
        widgets = {
            'rut':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: 11111111-1'}),
            'nombres':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: Jorge'}),
            'apellido_p':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: Salinas'}),
            'apellido_m':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: Fuentes'}),
            'fecha_nacimiento':forms.DateInput(attrs={'class':'form-control mb-2','placeholder':'Ej: DD/MM/AAAA'}),
            'correo':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: correo_ejemplo@ejemplo.com'}),
            'celular':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: +56967878678'}),
            'direccion':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: Avda. Vicuña Mackena 1010'}),
            'genero':forms.RadioSelect(attrs = {'class':'form-check-input'},choices=GENERO_OPCIONES),
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


       
    