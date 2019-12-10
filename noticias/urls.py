from django.urls import path
from . import views
from .views import NoticiaListView,NoticiaDetailView,NoticiaCreateView,NoticiaUpdateView,NoticiaDeleteView

noticias_patterns = ([
    path('', NoticiaListView.as_view(), name='noticias'),
    path('<int:pk>', NoticiaDetailView.as_view(), name='noticia'),
    path('create/', NoticiaCreateView.as_view(), name = 'create'),
    path('update/<int:pk>/', NoticiaUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', NoticiaDeleteView.as_view(),name='delete')
],'noticias')