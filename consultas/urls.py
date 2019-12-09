from django.urls import path
from .views import historial_pacientes,buscar_paciente_si_existe, info_paciente, nuevo_paciente,agregar_consulta,imprimir_pdf_receta,ver_ficha_paciente

consultas_patterns = ([
    path('', buscar_paciente_si_existe, name='buscar_paciente'),
    path('paciente/<int:pk>', info_paciente, name='info_paciente'),
    path('npaciente/',nuevo_paciente, name='nuevo_paciente'),
    path('agregar_consulta/<int:pk>',agregar_consulta, name='realizar_consulta'),
    path('ficha_paciente/<int:pk>',ver_ficha_paciente,name='ficha'),
    path('imprimir/<int:pk>',imprimir_pdf_receta,name='imprimir'),
    path('historial_pacientes/',historial_pacientes,name='historial_p')
],'consultas')