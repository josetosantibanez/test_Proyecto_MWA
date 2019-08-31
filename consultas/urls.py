from django.urls import path
from . import views
from .views import 

eventos_patterns = ([
    path('', EventoListView.as_view(), name='eventos'),
],'consultas')