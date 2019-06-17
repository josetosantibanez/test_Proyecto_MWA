from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .forms import MiembroForm
from .models import Miembro



# Create your views here.

class StaffRequiredMixin(object):
    """Este mixin requerira que el usuario sea miembro del staff"""
    @method_decorator(staff_member_required)
    def dispatch(self,request,*args,**kwargs):
        return super(StaffRequiredMixin,self).dispatch(request,*args,**kwargs)

@method_decorator(staff_member_required,name='dispatch')
class MiembroListView(ListView):
    model = Miembro

def agregar_miembro(request):
    args = {}
    if request.method == 'POST':
        form = MiembroForm(request.POST)
        if form.is_valid():     
            form.save()
            return redirect('miembros:miembros')
    else:
        form = MiembroForm()
    args['form'] = form
    return render(request,'miembros/miembro_form.html',args)


@method_decorator(staff_member_required,name='dispatch')
class MiembroDetailView(DetailView):
    model = Miembro

# @method_decorator(staff_member_required,name='dispatch')
# class MiembroCreateView(CreateView):
#     model = Miembro
#     form_class = MiembroForm
#     success_url = reverse_lazy('miembros:miembros')

@method_decorator(staff_member_required,name='dispatch')
class MiembroUpdateView(UpdateView):
    model = Miembro
    form_class = MiembroForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('miembros:update', args=[self.object.id])+'?ok'

@method_decorator(staff_member_required,name='dispatch')
class MiembroDeleteView(DeleteView):
    model = Miembro
    success_url = reverse_lazy('miembros:miembros')