from django.contrib import admin
from .models import Noticia

# Register your models here.

class NoticiasAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated','club_id']


    class Media:
        css = {
            'all': ('noticias/css/custom_ckeditor.css',)
        }
admin.site.register(Noticia,NoticiasAdmin)