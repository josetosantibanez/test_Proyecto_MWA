from django.urls import path
from . import views
from .views import buscar_paciente_si_existe, info_paciente, nuevo_paciente,agregar_consulta

consultas_patterns = ([
    path('', buscar_paciente_si_existe, name='buscar_paciente'),
    path('paciente/<int:pk>', info_paciente, name='info_paciente'),
    path('npaciente/',nuevo_paciente, name='nuevo_paciente'),
    path('agregar_consulta/<int:pk>',agregar_consulta, name='realizar_consulta')
],'consultas')