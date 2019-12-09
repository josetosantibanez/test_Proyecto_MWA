from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from .forms import BuscarPaciente,InfoPaciente,NuevoPaciente,AgregarConsulta
from .models import Paciente, Consulta
from registration.models import Profile
#Imprimir PDF
import io
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4



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
            break
        else:
            form = InfoPaciente()

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
    id_paciente  = get_object_or_404(Paciente,user=pk)
    # id_paciente = Paciente.objects.get(user=pk)
    if request.method == 'POST':
        form = AgregarConsulta(request.POST)
        request.POST._mutable= True
        request.POST['paciente']=id_paciente.id
        request.POST['medico']=request.user.id
        if form.is_valid():
            form.save()
            return redirect('consultas:ficha',pk=id_paciente.id)
        else:
            print(form.errors)
    else:
        form = AgregarConsulta()
    ctx={'form':form,'pk':pk}
    return render(request,'consultas/registrar_consulta.html',ctx)

def ver_ficha_paciente(request,pk):
    paciente = get_object_or_404(Paciente,pk=pk)
    consultas = Consulta.objects.all()
    if request.method == 'POST':
        if '_imprimir' in request.POST:
            c = Consulta.objects.raw('''select * from consultas_consulta where medico_id = 16
                                            order by created DESC limit 1''')[0]
            pk=c.id
            return redirect('consultas:imprimir',pk=pk)
            
        elif '_volver' in request.POST:
            return redirect('consultas:buscar_paciente')
    ctx={
        'pk':pk,
        'paciente':paciente,
        'consultas':consultas,
    }
    return render(request,'consultas/ficha_paciente.html',ctx)


def imprimir_pdf_receta(request,pk):
    consulta = get_object_or_404(Consulta,pk=pk)
    medico = get_object_or_404(User,pk=consulta.medico_id)

    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='attachement; filename=receta_med.pdf'
     # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer,pagesize=A4)

    p.setLineWidth(.3)
    p.setFont('Helvetica',22)
    p.drawString(30,750,'Receta Medica')
    p.setFont('Helvetica',12)
    p.drawString(30,735,medico.username)


    fecha = consulta.created
    fecha_f = fecha.strftime('%d/ %m/ %Y')
    p.setFont('Helvetica-Bold',12)
    p.drawString(480,750,fecha_f)
    p.line(460,747,560,747)
    
    
    p.save()
    pdf=buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

def historial_pacientes(request):
 
    pacientes = Consulta.objects.raw('''select MAX(c.created) as fecha,c.id,p.id, p.nombres, p.apellido_p, 
                                        p.apellido_m, p.rut from consultas_paciente p 
                                        inner join consultas_consulta c 
                                        where c.paciente_id = p.id group by p.rut;''')
    ctx={'pacientes':pacientes,}
    return render(request,'consultas/historial_pacientes.html',ctx)