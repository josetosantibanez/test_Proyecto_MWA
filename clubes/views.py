from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from .models import Club

# Create your views here.

def listado_clubes(request):
    clubes = Club.objects.all()
    return render(request,'clubes/listado_clubes.html',{'clubes':clubes})

def detail_club(request,pk):
    club = get_object_or_404(Club, pk=pk)
    return render(request,'clubes/detail_clubes.html',{'club':club})