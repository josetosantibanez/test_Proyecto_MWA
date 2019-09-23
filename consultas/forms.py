from django import forms
from .models import Paciente,Consulta
from itertools import cycle
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from registration.models import Profile


class AgregarConsulta(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente','medico','anotaciones','diagnostico','prescripcion']
        widgets = {
            'paciente':forms.HiddenInput(),
            'medico':forms.HiddenInput(),
            'anotaciones':forms.Textarea(attrs={'class':'form-control mb-2',}),
            'diagnostico':forms.Textarea(attrs={'class':'form-control mb-2',}),
            'prescripcion':forms.Textarea(attrs={'class':'form-control mb-2',}),
        }

class BuscarPaciente(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['rut']
        widgets = {
            'rut':forms.TextInput(attrs={'class':'form-control mb-2'}),
        }

class InfoPaciente(forms.ModelForm):
    class Meta:
        model = Paciente
        GENERO=[
            ('M','Masculino'),
            ('F','Femenino'),
        ]

        fields = ['rut','nombres','apellido_p','apellido_m','fecha_nacimiento',
        'correo','celular','direccion','genero','user']
        
        widgets = {
            'rut':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: 11111111-1'}),
            'nombres':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: Jorge'}),
            'apellido_p':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: Salinas'}),
            'apellido_m':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: Fuentes'}),
            'fecha_nacimiento':forms.DateInput(attrs={'class':'form-control mb-2','placeholder':'Ej: DD/MM/AAAA','readonly':'true'}),
            'correo':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: correo_ejemplo@ejemplo.com'}),
            'celular':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: +56967878678'}),
            'direccion':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: Avda. Vicuña Mackena 1010'}),
            'genero':forms.RadioSelect(attrs = {'class':'form-check-input'},choices=GENERO),
            'user':forms.HiddenInput()
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

    


class NuevoPaciente(forms.ModelForm):
    class Meta:
        model = Paciente
        GENERO=[
            ('M','Masculino'),
            ('F','Femenino'),
        ]

        fields = ['rut','nombres','apellido_p','apellido_m','fecha_nacimiento',
        'correo','celular','direccion','genero','user']
        
        widgets = {
            'rut':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: 11111111-1'}),
            'nombres':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: Jorge'}),
            'apellido_p':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: Salinas'}),
            'apellido_m':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: Fuentes'}),
            'fecha_nacimiento':forms.DateInput(attrs={'class':'form-control mb-2','placeholder':'Ej: DD/MM/AAAA'}),
            'correo':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: correo_ejemplo@ejemplo.com'}),
            'celular':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: +56967878678'}),
            'direccion':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: Avda. Vicuña Mackena 1010'}),
            'genero':forms.RadioSelect(attrs = {'class':'form-check-input'},choices=GENERO),
            'user':forms.HiddenInput()
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



    def clean_rut(self):
        rut = self.cleaned_data['rut']
        profiles = Profile.objects.all()
        
        rut = rut.upper()
        rut = rut.replace("-","")
        rut = rut.replace(".","")
        aux = rut[:-1]
        dv = rut[-1:]
    
        revertido = map(int, reversed(str(aux)))
        factors = cycle(range(2,8))
        s = sum(d * f for d, f in zip(revertido,factors))
        res = (-s)%11
    
        if str(res) == dv:
            pass
        elif dv=="K" and res==10:
            pass
        else:
            
            raise ValidationError("El rut ingresado no es válido")

        for profile in profiles:
            if profile.rut == rut:
                raise ValidationError("El rut ingresado ya esta registrado")
                break
        return rut

