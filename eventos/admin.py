from django.contrib import admin
from .models import Evento

# Register your models here.

class EventosAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated','club_id')


admin.site.register(Evento,EventosAdmin)