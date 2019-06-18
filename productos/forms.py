from django import forms
from .models import Producto, Reserva

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

        fields = ['cantidad_reservar']
        widgets = {
            'cantidad_reservar':forms.NumberInput(attrs={'class':'form-control'}),
            # 'estado':forms.RadioSelect(attrs = {'class':'form-check-input'},choices=ESTADO_OPCIONES),
        }