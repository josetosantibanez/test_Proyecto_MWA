from django.db import models

from django.contrib.auth.models import User
from consultas.models import Paciente


# Create your models here.

class Horario_disponible(models.Model):
    # Esta clase corresponde a los horarios que dispondra el medico como disponible para sus consultas
    # Esto tendra la duracion de cada bloque, su fecha, hora de inicio y hora de temrino, estado del horario
    # (si esta disponible u ocupado) y el medico que dispuso ese horario
    # 
    # La idea sera crear un registro por cada bloque que el medico escoja como disponible
    medico = models.ForeignKey(User, verbose_name="Medico", on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha consulta")
    hora_inicio = models.TimeField(verbose_name="Hora inicio de consulta")
    hora_termino = models.TimeField(verbose_name="Hora termino de consulta")
    duracion = models.IntegerField(verbose_name="Duracion de la consulta")
    estado = models.BooleanField(verbose_name="Estado")

class Horario_reservado(models.Model):
    # Esta clase registrara los horarios que hayan sido reservados registrando el horario en el que 
    # se hizo el registro junto con el paciente que hizo la reserva y el horario en cuestion
    horario = models.ForeignKey(Horario_disponible, verbose_name="Horario seleccionado", on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, verbose_name="Paciente", on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de reserva consulta")
    