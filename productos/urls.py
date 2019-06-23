from django.urls import path
from . import views
from .views import agregar_producto,estado_reservas,mis_reservas,ReservaListView ,ProductoListView, ProductoUpdateView, ProductoDeleteView, reservar_producto,ReservaListView

productos_patterns = ([
    path('', ProductoListView.as_view(), name='productos'),
    path('<int:pk>/', reservar_producto, name='producto'),
    path('create/', agregar_producto, name = 'create'),
    path('update/<int:pk>/', ProductoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductoDeleteView.as_view(),name='delete'),
    path('reservas',ReservaListView.as_view(),name='reservas'),
    path('estado_reservas/<int:pk>/',estado_reservas,name='estado_reservas'),
    path('misreservas/', ReservaListView.as_view() ,name='mis_reservas')
],'productos')