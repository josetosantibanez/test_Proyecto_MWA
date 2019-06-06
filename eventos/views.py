from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .forms import EventoForm
from .models import Evento

# Create your views here.

class StaffRequiredMixin(object):
    """Este mixin requerira que el usuario sea miembro del staff"""
    @method_decorator(staff_member_required)
    def dispatch(self,request,*args,**kwargs):
        return super(StaffRequiredMixin,self).dispatch(request,*args,**kwargs)

@method_decorator(staff_member_required,name='dispatch')
class EventoListView(ListView):
    model = Evento

@method_decorator(staff_member_required,name='dispatch')
class EventoDetailView(DetailView):
    model = Evento

@method_decorator(staff_member_required,name='dispatch')
class EventoCreateView(CreateView):
    model = Evento
    form_class = EventoForm
    success_url = reverse_lazy('eventos:eventos')

@method_decorator(staff_member_required,name='dispatch')
class EventoUpdateView(UpdateView):
    model = Evento
    form_class = EventoForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('eventos:update', args=[self.object.id])+'?ok'

@method_decorator(staff_member_required,name='dispatch')
class EventoDeleteView(DeleteView):
    model = Evento
    success_url = reverse_lazy('eventos:eventos')