from django import template
from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag
def get_usuario_list():
    usuario = User.objects.all()
    return usuarios