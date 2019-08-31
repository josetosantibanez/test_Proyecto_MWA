from django import forms
from .models import Miembro
from django.core.exceptions import ValidationError
from itertools import cycle
import datetime
from datetime import date

class MiembroForm(forms.ModelForm):
    class Meta:
        
        model = Miembro

        GENERO=[
            ('M','Masculino'),
            ('F','Femenino'),
        ]

        fields = ['rut','nombres','apellido_p','apellido_m','fecha_nacimiento',
        'correo','celular','direccion','dosis_diaria','fecha_expiracion_receta','genero','user_id']
        
        widgets = {
            'rut':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: 11111111-1'}),
            'nombres':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: Jorge'}),
            'apellido_p':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: Salinas'}),
            'apellido_m':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: Fuentes'}),
            'fecha_nacimiento':forms.DateInput(attrs={'class':'form-control mb-2','placeholder':'Ej: DD/MM/AAAA'}),
            'correo':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: correo_ejemplo@ejemplo.com'}),
            'celular':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: +56967878678'}),
            'direccion':forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Ej: Avda. Vicuña Mackena 1010'}),
            'dosis_diaria':forms.NumberInput(attrs={'class':'form-control mb-2'}),
            'fecha_expiracion_receta':forms.DateInput(attrs={'class':'form-control mb-2','placeholder':'Ej: DD/MM/AAAA'}),
            'genero':forms.RadioSelect(attrs = {'class':'form-check-input'},choices=GENERO),
            'user_id':forms.HiddenInput(attrs = {'value':14})
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
        miembros = Miembro.objects.all()
        
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

        for miembro in miembros:
            if miembro.rut == rut:
                raise ValidationError("El rut ingresado ya esta registrado")
                break
        return rut

    def clean_fecha_nacimiento(self):
        fecha = self.cleaned_data['fecha_nacimiento']
        fecha_actual = datetime.date.today()
        diferencia = (fecha_actual - fecha).days

        if diferencia < 6570:
            raise ValidationError("Debe ser mayor de edad para ingresar como miembro")
        else:
            pass

        return fecha

    def clean_fecha_expiracion_receta(self):
        fecha = self.cleaned_data['fecha_expiracion_receta']
        fecha_actual = datetime.date.today()
        diferencia = (fecha_actual - fecha).days
        if diferencia >= 0:
            raise ValidationError("Receta ya expirada")
        else:
            pass
        return fecha
       
    