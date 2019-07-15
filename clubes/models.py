from django.db import models
from django.contrib.auth.models import User

class Club(models.Model):
    rut_org = models.CharField(max_length = 11, verbose_name = "Rut organizacion")
    nombre_org = models.CharField(max_length = 200, verbose_name = "Nombre organizacion")
    direccion = models.CharField(max_length = 200, verbose_name = "Direccion club")
    telefono_contacto = models.CharField(max_length = 20, verbose_name = "Telefono de contacto")
    correo_contacto = models.CharField(max_length = 200, verbose_name = "Email de contacto")
    cant_max_miembros = models.SmallIntegerField(verbose_name="Cantidad maxima de miembros")
    cantidad_miembros = models.SmallIntegerField(verbose_name="Cantidad actual de miembros", default=0)
    usuario = models.OneToOneField(User, verbose_name = "Cuenta de usuario del club",default=1, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creacion")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de ult. actualizacion")

    class Meta:
        verbose_name = "Club"
        verbose_name_plural = "Clubes"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre_org
    