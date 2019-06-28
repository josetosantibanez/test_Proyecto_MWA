from django import template
from eventos.models import Evento, Asistentes

register = template.Library()

@register.simple_tag
def get_evento_list():
    eventos = Evento.objects.all()
    return eventos

@register.simple_tag
def get_asistentes_list():
    asistentes = Asistentes.objects.all()
    return asistentes