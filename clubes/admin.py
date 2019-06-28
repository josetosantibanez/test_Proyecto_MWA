from django.contrib import admin
from .models import Club

class ClubAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated','usuario')
    list_display = ('nombre_org', 'rut_org', 'correo_contacto','direccion')
    ordering = ('nombre_org',)
    search_fields = ('nombre_org','rut_org')


admin.site.register(Club,ClubAdmin)
