from django import forms
from .models import Miembro

class MiembroForm(forms.ModelForm):



    class Meta:
        
        model = Miembro
        BIRTH_YEAR_CHOICES=[
            '1997','1998','1999','2000'
        ]

        GENERO_OPCIONES=[
            ('M','Masculino'),
            ('F','Femenino'),
        ]
        fields = ['rut','nombres','apellido_p','apellido_m','fecha_nacimiento',
        'correo','celular','direccion','genero']
        widgets = {
            'rut':forms.TextInput(attrs={'class':'form-control mb-2'}),
            'nombres':forms.TextInput(attrs={'class':'form-control mb-2'}),
            'apellido_p':forms.TextInput(attrs={'class':'form-control mb-2'}),
            'apellido_m':forms.TextInput(attrs={'class':'form-control mb-2'}),
            'fecha_nacimiento':forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES),
            'correo':forms.TextInput(attrs={'class':'form-control mb-2'}),
            'celular':forms.TextInput(attrs={'class':'form-control mb-2'}),
            'direccion':forms.TextInput(attrs={'class':'form-control mb-2'}),
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
       
    