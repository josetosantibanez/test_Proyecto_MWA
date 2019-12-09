from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User

from datetime import datetime
from datetime import timedelta

# Create your views here.

def seleccionar_semana(request):
    today = date.today()
    m1=today.month
    if today.day == 31:
        d = 28
    else:
        d = 31
    m2 = today.month + deltatime(days=d)
    m3 = today.month + deltatime(days=31)
    meses = [today.month, today.month + deltatime(month=1), today.month + deltatime(month=2) ]
    return render(request, "horarios/seleccionar_semana.html")

def seleccionar_horarios_consultas(request):
    return render(request, html , ctx)