from django.contrib import admin
from .models import Producto, Reserva

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    read_only_fields = ['created','updated','club_id']

class ReservaAdmin(admin.ModelAdmin):
    read_only_fields = ['created','updated']

admin.site.register(Producto,ProductoAdmin)