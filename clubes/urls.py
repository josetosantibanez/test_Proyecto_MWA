from django.urls import path
from . import views
from .views import listado_clubes, detail_club 


clubes_patterns = ([
    path('', listado_clubes, name='clubes'),
    path('detail/<int:pk>',detail_club,name='club')
],'clubes')