from django.db import models
from clubes.models import Club
from django.contrib.auth.models import User

# Create your models here.

class Miembro(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creacion")
    updated = models.DateTimeField(auto_now = True, verbose_name= "Fecha de ult. actualizacion")
    rut = models.CharField(max_length=12, verbose_name = "Rut")
    nombres = models.CharField(max_length=40, verbose_name = "Nombres")
    apellido_p = models.CharField(max_length=20, verbose_name = "Apellido paterno")
    apellido_m = models.CharField(max_length=20, verbose_name = "Apellido materno")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    correo = models.CharField(max_length=100, verbose_name = "Correo electronico")
    celular = models.CharField(max_length=12, verbose_name = "Numero celular")
    direccion = models.CharField(max_length=200, verbose_name = "Direccion")
    genero = models.CharField(max_length=15, verbose_name = "Genero")
    dosis_diaria = models.SmallIntegerField(verbose_name="Dosis diaria recetada",default = 0)
    fecha_expiracion_receta = models.DateField(verbose_name="Fecha de expiración de receta", blank=True, null=True)
    receta = models.FileField(verbose_name="Receta",upload_to="miembros", blank=True, null=True)
    fotocopia_carnet_a = models.FileField(verbose_name="Fotocopia de carnet A",upload_to="miembros", blank=True, null=True)
    fotocopia_carnet_b = models.FileField(verbose_name="Fotocopia de carnet B",upload_to="miembros", blank=True, null=True)
    club_id = models.ForeignKey(Club,verbose_name="Club",on_delete=models.CASCADE,default=1)
    user_id = models.OneToOneField(User,verbose_name = "Usuario", on_delete=models.CASCADE, default = 99)


    class Meta:
        verbose_name = "Miembro"
        verbose_name_plural = "Miembros"
        ordering = ['apellido_p']

    def __str__(self):
        ret = self.apellido_p + " " + self.nombres
        return ret
    