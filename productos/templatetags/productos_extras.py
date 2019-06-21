from django import template
from productos.models import Producto, Reserva

register = template.Library()

@register.simple_tag
def get_producto_list():
    productos = Producto.objects.all()
    return productos

@register.simple_tag
def get_reservas_list():
    reservas = Reserva.objects.all()
    return reservas