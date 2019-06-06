from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .forms import NoticiaForm
from .models import Noticia

# Create your views here.

class StaffRequiredMixin(object):
    """Este mixin requerira que el usuario sea miembro del staff"""
    @method_decorator(staff_member_required)
    def dispatch(self,request,*args,**kwargs):
        return super(StaffRequiredMixin,self).dispatch(request,*args,**kwargs)

class NoticiaListView(ListView):
    model = Noticia

class NoticiaDetailView(DetailView):
    model = Noticia

@method_decorator(staff_member_required,name='dispatch')
class NoticiaCreateView(CreateView):
    model = Noticia
    form_class = NoticiaForm
    success_url = reverse_lazy('noticias:noticias')

@method_decorator(staff_member_required,name='dispatch')
class NoticiaUpdateView(UpdateView):
    model = Noticia
    form_class = NoticiaForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('noticias:update', args=[self.object.id])+'?ok'

@method_decorator(staff_member_required,name='dispatch')
class NoticiaDeleteView(DeleteView):
    model = Noticia
    success_url = reverse_lazy('noticias:noticias')