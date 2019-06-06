from django.contrib import admin
from .models import Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    read_only_fields = ['created','updated','club_id']

admin.site.register(Producto,ProductoAdmin)