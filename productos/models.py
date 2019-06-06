from django.db import models
from clubes.models import Club

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=200,verbose_name="Producto")
    proporcion = models.CharField(max_length=200,verbose_name="Proporcion en % (Indica/Sativa/Rudelaris)")
    descripcion = models.TextField(verbose_name="Descripción")
    stock = models.SmallIntegerField(verbose_name="Stock disponible(Gramos)")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="productos")
    club_id = models.ForeignKey(Club, verbose_name = "Codigo de club",on_delete=models.CASCADE,default=1)
    created = models.DateTimeField(auto_now_add= True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now= True,verbose_name="Fecha de ult. actualizacion")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['updated', 'created']

    
    def __str__(self):
        return self.nombre