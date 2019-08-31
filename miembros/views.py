from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import MiembroForm
from .models import Miembro
from registration.forms import UserCreationHidden



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
    users = User.objects.all()
    am = get_object_or_404(User,pk=14)
    if request.method == 'POST':
        print(am.id)
        request.POST._mutable = True
        request.POST['user_id'] = am.id
        form = MiembroForm(request.POST)
        print("Quie")
        print(form)
        if form.is_valid():
            print("Formulario es valido")
            f=form.save(commit=False)#Guardamos sin guardar 
            ### Trigger user de miembro
            f.user_id = 0
            for u in users:
                
                if u.username == f.rut:
                    # Existe un cuenta de usuario con este rut, 
                    # debo enlazar este nuevo miembro cn la cuenta y hacer break
                    print("Si!!!!!!!!!!!!!!!!!!!1")
                    f.user_id=u.id
                    break
                else:
                    print("No")
                    pass
            if f.user_id == 0:
                #Si aun sigue siendo 0 es porque no existe una cuenta con ese rut
                #Entonces debemos crear la cuenta
                print("Entramos a donde creariamos la cuenta")
                userform = UserCreationFormHidden()


                vari = f.rut[0:5]
                userform.username = f.rut
                userform.email = f.correo
                userform.password_1 = vari
                userform.username = vari
                userform.save()
            f.save()
            return redirect('miembros:miembros')
    else:
        form = MiembroForm()
    args={'form':form}
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