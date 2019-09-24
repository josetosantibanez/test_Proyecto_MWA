from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from .forms import BuscarPaciente,InfoPaciente,NuevoPaciente,AgregarConsulta
from .models import Paciente
from registration.models import Profile

# Create your views here.


def buscar_paciente_si_existe(request):
    #Buscaremos si el paciente ya tiene cuenta en mwa, en caso de si tener cuenta redireccionamos a un
    #modificar que permita ver los datos actuales del paciente, si tiene todos sus datos se mostraran
    #solo readonly, en caso de faltar alguno esos se podran colocar y los que ya esten readonly
    if request.method == 'POST':
        usuarios = User.objects.all()
        form = BuscarPaciente(request.POST)
        print("Hasta aca todo bien")
        for usuario in usuarios:

            if usuario.profile.tipo_cuenta_id == 1:

                print("usuario {} request {}".format(usuario.username,request.POST['rut']))
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
    p = get_object_or_404(User,pk=pk)
    profiles = Profile.objects.all()
    print("paciente {}".format( p.username))
    for profile in profiles:
        if profile.user_id == p.id:
            print("Victoriaaaa")
            form = InfoPaciente(instance=profile)
            rut = profile.rut
            nombres = profile.nombres
            apellido_p = profile.apellido_p
            apellido_m = profile.apellido_m
            fecha_nacimiento = profile.fecha_nacimiento
            user = profile.user_id
        else:
            form = InfoPaciente()
            print("Entro al else")

    if request.method=='POST':

        form = InfoPaciente(request.POST,instance=profile)
        request.POST._mutable=True
        request.POST['rut'] = rut
        request.POST['nombres'] = nombres
        request.POST['apellido_p'] = apellido_p
        request.POST['apellido_m'] = apellido_m
        request.POST['fecha_nacimiento'] = fecha_nacimiento
        request.POST['fecha_nacimiento'] = fecha_nacimiento
        request.POST['user'] = user
        if form.is_valid():
            print("Validisimo viejo")
            form.save()
            return redirect('consultas:realizar_consulta',pk=user)
        else:
            print('NO FUE VALIDO PQ {}'.format(form.errors))
    ctx={'form':form,'pk':pk}
    return render(request,'consultas/datos_paciente.html',ctx)
    #Para que esto funcione necesitaremos que profile tenga los datos de persona.


def nuevo_paciente(request):
    if request.method == 'POST':
        form = NuevoPaciente(request.POST)
        request.POST._mutable = True
        request.POST['user'] = 14
        if form.is_valid():
            print("Formulario valido")
            form.save()
            return redirect('consultas:realizar_consulta',pk=user)#configurar url
        else:
            print('NO FUE VALIDO PQ {}'.format(form.errors))
    else:
        form = NuevoPaciente()
    ctx = {'form':form}
    return render(request,'consultas/nuevo_paciente.html',ctx)


def agregar_consulta(request,pk):
    user_paciente = get_object_or_404(User, pk=pk)
    id_paciente = Paciente.objects.get(user=pk)
    print(id_paciente)
    if request.method == 'POST':
        form = AgregarConsulta(request.POST)
        request.POST._mutable= True
        request.POST['paciente']=id_paciente.id
        request.POST['medico']=request.user.id
        if form.is_valid():
            
            form.save()
            return redirect('consultas:buscar_paciente')
            #Falta imprimir receta
        else:
            print(form.errors)
    else:
        form = AgregarConsulta()
    ctx={'form':form,'pk':pk}
    return render(request,'consultas/registrar_consulta.html',ctx)
