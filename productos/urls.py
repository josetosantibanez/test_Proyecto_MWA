from django.urls import path
from . import views
from .views import agregar_producto, ProductoListView, ProductoUpdateView, ProductoDeleteView, reservar_producto,ver_reservas

productos_patterns = ([
    path('', ProductoListView.as_view(), name='productos'),
    path('<int:pk>/', reservar_producto, name='producto'),
    path('create/', agregar_producto, name = 'create'),
    path('update/<int:pk>/', ProductoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductoDeleteView.as_view(),name='delete'),
    path('reservas',ver_reservas,name='reservas')
],'productos')