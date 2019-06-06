from django.urls import path, include

from .views import HomePageView, InicioPageView


urlpatterns = [
    path('', InicioPageView.as_view(), name="inicio"),
    path('club/', HomePageView.as_view(), name="home"),
    
]