from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .forms import ProductoForm, ReservaForm, ListadoReservaForm
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

def agregar_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("productos:productos")
    else:
        form = ProductoForm()
    return render(request,'productos/producto_form.html',{'form':form})    

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
    miembros = Miembro.objects.all() #Se puede mejorar
    if request.method == "POST":
        print("Entro al post, {}".format(request.user))
        request.POST._mutable = True
        res = request.POST['cantidad_reservar']
        cant =  int(res) * producto.precio_gramo
        request.POST['precio_total'] = cant
        request.POST['usuario'] = request.user.id
        request.POST['producto'] = producto.id
        request.POST['estado'] = 'D'
        producto.stock = producto.stock - int(res)
        form = ReservaForm(request.POST)
        print(producto.precio_gramo)
        print(res)
        print(cant)
        if form.is_valid():            
            print("Formulario valido")
            form.save()
            producto.save()
            return redirect('productos:productos')
    else:
        print("Renderizando la pagina")
        
        form = ReservaForm()
    if request.user.profile.tipo_cuenta_id == 1:
        for miembro in miembros:
            if miembro.user_id_id == request.user.id:
                m = get_object_or_404(Miembro,pk=miembro.id)
                cmax = m.dosis_diaria * 14
    else:
        m={}
        cmax = 0                
    contexto = {
        'form':form,'producto':producto,'m':m,'cmax':cmax
    }
    return render (request,'productos/producto_detail.html',contexto)

class ReservaListView(ListView):
    model = Reserva

def mis_reservas(request):
    return render(request,'productos/mis_reservas.html')
    
def estado_reservas(request, pk):
    reserva = get_object_or_404(Reserva,pk=pk)
    p = get_object_or_404(Producto,pk=reserva.producto_id)
    if request.method == "POST":
        request.POST._mutable = True
        request.POST['usuario'] = reserva.usuario_id
        request.POST['producto'] = reserva.producto_id
        request.POST['cantidad_reservar'] = reserva.cantidad_reservar
        request.POST['precio_total'] = reserva.precio_total
        res=request.POST['cantidad_reservar']
        if '_entregado' in request.POST:
            print("E")
            request.POST['estado'] = 'E'
        elif '_cancelar' in request.POST:
            print("C")
            request.POST['estado'] = 'C'
            p.stock = p.stock + int(res)
            print(request.POST['estado'])
        elif '_despachado' in request.POST:
            print("D")
            request.POST['estado'] = 'D'
        form = ListadoReservaForm(request.POST,instance=reserva)
        if form.is_valid():
            form.save()
            p.save()
            print(request.POST['estado'])
        return redirect('productos:reservas')
    else:
        form = ListadoReservaForm()
    return render(request, 'productos/reserva_detalle.html',{'form':form,'reserva':reserva})

    
            
            