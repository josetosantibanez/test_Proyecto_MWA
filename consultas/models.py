from django.db import models
from django.contrib.auth.models import User

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
    user = models.ForeignKey(User,verbose_name = "Cuenta de usuario", on_delete=models.CASCADE, default=200)
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creacion")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de ult. actualizacion")

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente,verbose_name ="Paciente atendido",on_delete=models.CASCADE)
    medico = models.ForeignKey(User,verbose_name="Medico",on_delete=models.CASCADE)
    anotaciones = models.TextField(verbose_name="Datos de la consulta")
    diagnostico = models.TextField(verbose_name="Diagnostico")
    prescripcion = models.TextField(verbose_name="Prescripcion")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creacion")
    updated = models.DateTimeField(auto_now = True, verbose_name = "Fecha de ult. actualizacion")
