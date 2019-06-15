from django.db import models

# Create your models here.

class Paciente(models.Model):
    rut = models.CharField(max_length=10, verbose_name = "Rut")
    nombres = models.CharField(max_length=40, verbose_name = "Nombres")
    apellido_p = models.CharField(max_length=20, verbose_name = "Apellido paterno")
    apellido_m = models.CharField(max_length=20, verbose_name = "Apellido materno")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    correo = models.CharField(max_length=100, verbose_name = "Correo electronico")
    celular = models.CharField(max_length=12, verbose_name = "Numero celular")
    direccion = models.CharField(max_length=200, verbose_name = "Direccion")
    genero = models.CharField(max_length=1, verbose_name = "Genero")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creacion")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de ult. actualizacion")



