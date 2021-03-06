from django.urls import path
from . import views
from .views import EventoListView, asistir_evento, EventoCreateView, EventoUpdateView, EventoDeleteView

eventos_patterns = ([
    path('', EventoListView.as_view(), name='eventos'),
    path('<int:pk>/', asistir_evento, name='evento'),
    path('create/', EventoCreateView.as_view(), name = 'create'),
    path('update/<int:pk>/', EventoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', EventoDeleteView.as_view(),name='delete')
],'eventos')