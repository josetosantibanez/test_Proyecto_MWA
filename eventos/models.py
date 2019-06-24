from django.db import models
from clubes.models import Club
from miembros.models import Miembro

# Create your models here.

class Evento(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Evento")
    cupos = models.SmallIntegerField(verbose_name="Cupos disponibles")
    fecha = models.DateTimeField(verbose_name="Fecha evento")
    ubicacion = models.CharField(max_length=200, verbose_name="Dirección evento")
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="eventos")
    club_id = models.ForeignKey(Club,verbose_name = "Codigo de club",on_delete=models.CASCADE,default=1)
    created = models.DateTimeField(auto_now_add= True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now= True,verbose_name="Fecha de ult. actualizacion")

    class Meta:
        verbose_name="Evento"
        verbose_name_plural = "Eventos"
        ordering = ['fecha']

    
    def __str__(self):
        return self.nombre


class Asistentes(models.Model):
    miembro = models.ForeignKey(Miembro,verbose_name="Miembro asitente", on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento,verbose_name="Evento", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add= True, verbose_name="Fecha de creacion")

    class Meta:
        verbose_name="Asistencia"
        verbose_name_plural = "Asistencias"
        ordering = ['miembro']

    
    def __str__(self):
        return self.miembro
