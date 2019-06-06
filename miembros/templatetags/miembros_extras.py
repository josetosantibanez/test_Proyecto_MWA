from django import template
from miembros.models import Miembro

register = template.Library()

@register.simple_tag
def get_miembro_list():
    miembros = Miembro.objects.all()
    return miembros