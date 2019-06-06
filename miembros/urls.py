from django.urls import path
from . import views
from .views import MiembroListView,MiembroDetailView,MiembroCreateView,MiembroUpdateView,MiembroDeleteView

miembros_patterns = ([
    path('', MiembroListView.as_view(), name='miembros'),
    path('<int:pk>/', MiembroDetailView.as_view(), name='miembro'),
    path('create/', MiembroCreateView.as_view(), name = 'create'),
    path('update/<int:pk>/', MiembroUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', MiembroDeleteView.as_view(),name='delete')
],'miembros')