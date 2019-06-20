from django import forms
from .models import Producto, Reserva
from miembros.models import Miembro
from django.core.exceptions import ValidationError

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre','proporcion','descripcion','stock','imagen']
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'proporcion':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control'}),
            'stock':forms.NumberInput(attrs={'class':'form-control'})
        }
        labels = {
            'nombre':'Producto' ,
            'proporcion':'Proporciones',
            'descripcion':'Descripción del producto',
            'stock':'Stock disponible',
            'imagen':'Imagen',
        }

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva

        ESTADO_OPCIONES=[
            ('P','Entrega pendiente'),
            ('E','Entregado'),
        ]

        fields = ['cantidad_reservar','estado','usuario','producto']
        widgets = {
            'cantidad_reservar':forms.NumberInput(attrs={'class':'form-control'}),
            'estado':forms.HiddenInput(),
            'usuario':forms.HiddenInput(),
            'producto':forms.HiddenInput(),
        }
    
    def clean_cantidad_reservar(self):
        cantidad = self.cleaned_data['cantidad_reservar']
        miembros = Miembro.objects.all()
        if cantidad <= 0:
            raise ValidationError("No puede reservar por 0 o menos")
        else:
            pass
        return cantidad

    # def clean(self):
    #     form_data = self.cleaned_data
    #     miembros = Miembro.objects.all()
    #     for miembro in miembros:
    #         if form_data['']
