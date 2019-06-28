from django import template
from clubes.models import Club

register = template.Library()

@register.simple_tag
def get_clubes_list():
    clubes = Club.objects.all()
    return clubes