from django.db import models
from clubes.models import Club
from django.contrib.auth.models import User


# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=200,verbose_name="Producto")
    proporcion = models.CharField(max_length=200,verbose_name="Proporcion en % (Indica/Sativa/Rudelaris)")
    descripcion = models.TextField(verbose_name="Descripción")
    stock = models.SmallIntegerField(verbose_name="Stock disponible(Gramos)")
    precio_gramo = models.IntegerField(verbose_name = "Precio por gramo", default=8000)
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

class Reserva(models.Model):
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE,default=1,blank=True,null=True)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE,default=1,blank=True,null=True)
    cantidad_reservar = models.SmallIntegerField(verbose_name="Cantidad a reservar")
    estado = models.CharField(max_length=1,verbose_name = "Estado",default='P')
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creacion")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de ult. actualizacion")

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ['created', 'updated']

    
    def __str__(self):
        return self.usuario