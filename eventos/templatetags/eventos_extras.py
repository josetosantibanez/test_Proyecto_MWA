from django import template
from eventos.models import Evento

register = template.Library()

@register.simple_tag
def get_evento_list():
    eventos = Evento.objects.all()
    return eventos