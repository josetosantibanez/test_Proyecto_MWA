from django.contrib import admin
from .models import Miembro, Club


# Register your models here.

class MiembrosAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated','club_id')




admin.site.register(Miembro,MiembrosAdmin)