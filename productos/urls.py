from django.urls import path
from . import views
from .views import ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView, reservar_producto

productos_patterns = ([
    path('', ProductoListView.as_view(), name='productos'),
    path('<int:pk>/', reservar_producto, name='producto'),
    path('create/', ProductoCreateView.as_view(), name = 'create'),
    path('update/<int:pk>/', ProductoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductoDeleteView.as_view(),name='delete')
],'productos')