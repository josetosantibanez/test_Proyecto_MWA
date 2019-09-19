from django.urls import path
from . import views
from .views import buscar_paciente_si_existe, info_paciente, nuevo_paciente

consultas_patterns = ([
    path('', buscar_paciente_si_existe, name='buscar_paciente'),
    path('paciente/<int:pk>', info_paciente, name='info_paciente'),
    path('npaciente/',nuevo_paciente, name='nuevo_paciente'),
],'consultas')