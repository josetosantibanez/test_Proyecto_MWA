from django import template
from noticias.models import Noticia

register = template.Library()

@register.simple_tag
def get_noticia_list():
    noticias = Noticia.objects.all()
    return noticias