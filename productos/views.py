from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .forms import ProductoForm, ReservaForm
from .models import Producto, Reserva
from miembros.models import Miembro

# Create your views here.

class StaffRequiredMixin(object):
    """Este mixin requerira que el usuario sea miembro del staff"""
    @method_decorator(staff_member_required)
    def dispatch(self,request,*args,**kwargs):
        return super(StaffRequiredMixin,self).dispatch(request,*args,**kwargs)

class ProductoListView(ListView):
    model = Producto

# class ProductoDetailView(DetailView):
#     model = Producto

@method_decorator(staff_member_required,name='dispatch')
class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('productos:productos')

@method_decorator(staff_member_required,name='dispatch')
class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('productos:update', args=[self.object.id])+'?ok'

@method_decorator(staff_member_required,name='dispatch')
class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy('productos:productos')

def reservar_producto(request,pk):
    producto = get_object_or_404(Producto,id=pk)
    if request.method == "POST":
        print("Entro al post")
        form = ReservaForm(request.POST)
        if form.is_valid():            
            print("Formulario valido")
            form = form.save(commit=False)
            form.usuario = request.user
            form.producto = producto
            form.estado = 'P'
            form.save()
    else:
        print("Renderizando la pagina")
        form = ReservaForm()
    return render (request,'productos/producto_detail.html',{'form':form,'producto':producto})
    
            
            