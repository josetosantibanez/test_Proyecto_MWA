from django import template
from productos.models import Producto

register = template.Library()

@register.simple_tag
def get_producto_list():
    productos = Producto.objects.all()
    return productos