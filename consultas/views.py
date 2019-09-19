from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from .forms import BuscarPaciente,InfoPaciente
from .models import Paciente

# Create your views here.


def buscar_paciente_si_existe(request):
    #Buscaremos si el paciente ya tiene cuenta en mwa, en caso de si tener cuenta redireccionamos a un
    #modificar que permita ver los datos actuales del paciente, si tiene todos sus datos se mostraran
    #solo readonly, en caso de faltar alguno esos se podran colocar y los que ya esten readonly
    if request.method == 'POST':
        usuarios = User.objects.all()
        form = BuscarPaciente(request.POST)
        for usuario in usuarios:
            if usuario.profile.tipo_cuenta_id == 1:
                if usuario.username == request.POST['rut']:
                    print("Paciente ya tiene una cuenta")
                    return redirect('consultas:info_paciente', pk=usuario.id)
                    #Aca redireccionamos y salimos de la funcion
        #Aca el paciente no tendria cuenta procederiamos a tomar sus datos para posteriormente crearle una
        print("Paciente no tiene cuenta")
        #Aca redireccionamos y salimos de la funcion
        return redirect('consultas:nuevo_paciente')
    else:
        form = BuscarPaciente()
        ctx = {'form':form}
        return render(request,'consultas/buscar_paciente.html',ctx)


def info_paciente(request,pk):
    paciente = get_object_or_404(User,pk=pk)
    form = InfoPaciente(paciente)
    ctx={'form':form,'pk':pk}
    return render(request,'consultas/datos_paciente.html',ctx)
    #Para que esto funcione necesitaremos que profile tenga los datos de persona.


def nuevo_paciente(request):
    if request.method == 'POST':
        form = InfoPaciente(request.POST)
        if form.is_valid():
            print("Formulario valido")
            form.save()
            return redirect('consultas:consultas')#configurar url
    else:
        form = InfoPaciente()
        ctx = {'form':form}
        return render(request,'consultas/datos_paciente.html',ctx)
