from django import forms
from .models import Producto, Reserva
from miembros.models import Miembro
from django.core.exceptions import ValidationError

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre','proporcion','descripcion','stock','imagen','precio_gramo']
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'proporcion':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control'}),
            'stock':forms.NumberInput(attrs={'class':'form-control'}),
            'imagen':forms.FileInput(attrs={'class':'form-control'}),
            'precio_gramo':forms.NumberInput(attrs={'class':'form-control'}),
        }
        labels = {
            'nombre':'Producto' ,
            'proporcion':'Proporciones',
            'descripcion':'Descripción del producto',
            'stock':'Stock disponible',
            'imagen':'Imagen',
            'precio_gramo':"Precio por gramo"
        }
    
    def clean_stock(self):
        stock = self.cleaned_data['stock']
        if stock <= 0:
            raise ValidationError("No se puede agregar un producto sin stock.")
        return stock
    
    def clean_precio_gramo(self):
        precio_gramo = self.cleaned_data['precio_gramo']
        if precio_gramo <= 0:
            raise ValidationError("El producto no puede tener un precio igual o menor a 0.")
        return precio_gramo

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
            raise ValidationError("No puede reservar por 0 o menos.")
        else:
            pass
        return cantidad

    def clean(self):
        form_data = self.cleaned_data
        miembros = Miembro.objects.all()
        productos = Producto.objects.all()
        c = form_data['cantidad_reservar']
        user = form_data['usuario']
        print("Entro a la validacion general")
        for miembro in miembros:
            print(user)
            print(miembro.user_id_id)
            if user.id == miembro.user_id_id:
                cant = miembro.dosis_diaria * 14
                print("Cantidad a reservar: {}".format(c))
                print("Cantidad maxima: {}".format(cant) )
                if c > cant:
                    self._errors['cantidad_reservar']=["La cantidad que desea reservar supera el maximo permitido de dos semanas de dosis."]
                    del form_data['cantidad_reservar']
                    break
                else:
                    for producto in productos:
                        if c > producto.stock:
                            self._errors['cantidad_reservar']=["La cantidad que desea reservar supera el stock disponible."]
                            del form_data['cantidad_reservar']
                            break
        return form_data


