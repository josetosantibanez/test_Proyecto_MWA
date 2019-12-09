from django.urls import path
from .views import seleccionar_semana,seleccionar_horarios_consultas

horarios_patterns = ([
    path('', seleccionar_semana, name='seleccionar_semana'),
],'horarios')