from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from medicalapp.models import *
from medicalapp.forms import *
from django.contrib.auth.decorators import login_required


#--------------------------------------------------------------------------------------

#Vista de inicio

def inicio(request):
    return render(request, "medicalapp/inicio.html", {'mensaje':"Bienvenido", 'mensaje2':"Inicia sesion para comenzar a operar!"})

#--------------------------------------------------------------------------------------

#Vista sobre mi

def sobremi(request):
    return render(request, "medicalapp/sobremi.html")


#--------------------------------------------------------------------------------------

#Vista de registro

def registro(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)  # Asegúrate de incluir request.FILES
        if form.is_valid():
            user = form.cleaned_data.get('username')
            user_instance = form.save()

            # Guarda el avatar si se proporcionó una imagen
            avatar = form.cleaned_data.get('avatar')
            if avatar:
                avatar_obj = Avatar(usuario=user_instance, imagen=avatar)
                avatar_obj.save()

            return render(request, 'medicalapp/inicio.html', {'mensaje': 'Usuario Creado!'})

    else:
        form = RegistrationForm()
    return render(request, 'medicalapp/users/register.html', {'form': form})

#--------------------------------------------------------------------------------------

#Vista de login

def iniciosesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data["username"]
            contra = form.cleaned_data["password"]
            user = authenticate(request, username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return render(request, "medicalapp/inicio.html", {'mensaje':'Bienvenido'})  
            else:
                return render(request, "medicalapp/inicio.html", {'mensaje':'Datos incorrectos'})
        else:
            mensaje = "Error, formulario erróneo"
    else:
        form = AuthenticationForm()
        
    return render(request, "medicalapp/users/login.html", {"form": form,})
    
   
#--------------------------------------------------------------------------------------

# Vista para editar el usuario

@login_required
def editar_usuario(request):
    usuario = request.user

    if request.method == 'POST':

        form = EditarUsuario(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            usuario.email = datos["email"]
            usuario.set_password(datos["password1"])
            usuario.first_name = datos["first_name"]
            usuario.last_name = datos["last_name"]

            usuario.save()

            return render(request, "medicalapp/inicio.html",{"mensaje":"Se guardaron tus cambios"})
        
    else:

        form = EditarUsuario(initial=
            {'email':usuario.email,
             'first_name':usuario.first_name,
             'last_name':usuario.last_name,
             }
                              )
    return render(request, "medicalapp/users/editarUsuario.html", {'form':form , 'usuario':usuario})

#--------------------------------------------------------------------------------------

# Vista para agregar el avatar

@login_required
def agregarAvatar(request):

    if request.method == "POST":

        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            usuarioActual = User.objects.get(username=request.user)
            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])
            avatar.save()
            return render(request, "medicalapp/inicio.html")
    else:
        form = AvatarForm()

    return render(request, "medicalapp/users/agregarAvatar.html", {"form":form})


#--------------------------------------------------------------------------------------

#Lista de pacientes y buscadores

@login_required
def lista_pacientes(request):
    #Lista
    pacientes = Pacientes.objects.all()

    #Formulario de busqueda por DNI
    if 'buscar_dni' in request.GET:
        form_dni = BusquedaDNI(request.GET)
        if form_dni.is_valid():
            dni = form_dni.cleaned_data['dni']
            pacientes = Pacientes.objects.filter(documento=dni)
    else:
        form_dni = BusquedaDNI()

    #Formulario de búsqueda por médico
    if 'buscar_medico' in request.GET:
        form_doc = BusquedaDoc(request.GET)
        if form_doc.is_valid():
            doc = form_doc.cleaned_data['doc']
            pacientes = Pacientes.objects.filter(medico=doc)
    else:
        form_doc = BusquedaDoc()

    return render(request, 'medicalapp/funciones/listaPacientes.html', {'form_dni' : form_dni , 'form_doc' : form_doc , 'pacientes': pacientes})


#--------------------------------------------------------------------------------------

#Lista de pacientes internados y buscadores

@login_required
def lista_internados(request):
    #Lista
    pacientes = PacientesInternados.objects.all()

    #Formulario de busqueda por DNI
    if 'buscar_dni' in request.GET:
        form_dni = BusquedaDNI(request.GET)
        if form_dni.is_valid():
            dni = form_dni.cleaned_data['dni']
            pacientes = PacientesInternados.objects.filter(documento=dni)
    else:
        form_dni = BusquedaDNI()

    #Formulario de búsqueda por médico
    if 'buscar_medico' in request.GET:
        form_doc = BusquedaDoc(request.GET)
        if form_doc.is_valid():
            doc = form_doc.cleaned_data['doc']
            pacientes = PacientesInternados.objects.filter(medico=doc)
    else:
        form_doc = BusquedaDoc()

        #Formulario de búsqueda por sala
    if 'buscar_sala' in request.GET:
        form_sala = BusquedaSala(request.GET)
        if form_sala.is_valid():
            sala = form_sala.cleaned_data['sala']
            pacientes = PacientesInternados.objects.filter(sala_asignada=sala)
    else:
        form_sala = BusquedaSala()


    return render(request, 'medicalapp/funciones/listaInternados.html', {'form_dni' : form_dni , 'form_doc' : form_doc , 'form_sala' : form_sala, 'pacientes': pacientes})

#--------------------------------------------------------------------------------------

#Lista de pacientes y buscadores

@login_required
def lista_hospitales(request):
    #Lista
    hospitales = Hospitales.objects.all()

    #Formulario de busqueda por ID
    if 'buscar_id' in request.GET:
        form_id = BusquedaId(request.GET)
        if form_id.is_valid():
            id = form_id.cleaned_data['id']
            hospitales = Hospitales.objects.filter(id=id)
    else:
        form_id = BusquedaId()

    #Formulario de búsqueda por localidad
    if 'buscar_localidad' in request.GET:
        form_loc = BusquedaLocalidad(request.GET)
        if form_loc.is_valid():
            localidad = form_loc.cleaned_data['localidad']
            hospitales = Hospitales.objects.filter(localidad=localidad)
    else:
        form_loc = BusquedaLocalidad()

    return render(request, 'medicalapp/funciones/listaHospitales.html', {'form_id' : form_id , 'form_loc' : form_loc , 'hospitales': hospitales})

#--------------------------------------------------------------------------------------

#Lista de pacientes y buscadores

@login_required
def lista_medicos(request):
    usuarios_sin_perfil = User.objects.filter(medicos__isnull=True)
    for usuario in usuarios_sin_perfil:
        medico = Medicos(user=usuario)
        medico.save()

    medicos = Medicos.objects.all()

        #Formulario de búsqueda por médico
    if 'buscar_medico' in request.GET:
        form_doc = BusquedaDoc(request.GET)
        if form_doc.is_valid():
            doc = form_doc.cleaned_data['doc']
            medicos = Medicos.objects.filter(numero_matricula=doc)
    else:
        form_doc = BusquedaDoc()


    return render(request, 'medicalapp/funciones/listaMedicos.html', {'form_doc':form_doc , 'medicos': medicos})



#--------------------------------------------------------------------------------------


#Vista de pacientes

@login_required
def paciente(request, paciente_id):
    paciente = get_object_or_404(Pacientes, pk=paciente_id)
    return render(request, 'medicalapp/funciones/paciente.html', {'paciente': paciente})

#--------------------------------------------------------------------------------------

#Eliminar Paciente

@login_required
def eliminar_paciente(request, pacienteDNI):
     paciente = Pacientes.objects.get(documento=pacienteDNI)
     paciente.delete()

     pacientes = Pacientes.objects.all()

     return redirect('ListaPacientes')


#--------------------------------------------------------------------------------------

#Eliminar Internado

@login_required
def eliminar_internado(request, pacienteDNI):
     paciente = PacientesInternados.objects.get(documento=pacienteDNI)
     paciente.delete()

     pacientes = PacientesInternados.objects.all()

     return redirect('ListaInternados')


#--------------------------------------------------------------------------------------

#Agregar un paciente a la BD

@login_required
def agregar_paciente(request):
    if request.method == 'POST':
        form = FormularioPacientes(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            medico_numero_matricula = datos['medico']
            medico = Medicos.objects.get(numero_matricula=medico_numero_matricula)
            paciente = Pacientes(
                documento=datos['documento'],
                nombre=datos['nombre'],
                apellido=datos['apellido'],
                sexo=datos['sexo'],
                nacimiento=datos['nacimiento'],
                u_consulta=datos['u_consulta'],
                medico=medico.numero_matricula 
            )
            paciente.save()
            return redirect('ListaPacientes')
    else:
        form = FormularioPacientes()
    return render(request, 'medicalapp/funciones/formPacientes.html', {'form': form})

#--------------------------------------------------------------------------------------

#Agregar un paciente internado a la BD

@login_required
def agregar_internado(request):
    if request.method == 'POST':

        form = FormularioInternados(request.POST)

        if form.is_valid():

            datos = form.cleaned_data
            medico_numero_matricula = datos['medico']
            medico = Medicos.objects.get(numero_matricula=medico_numero_matricula)

            paciente = Pacientes(
                documento=datos['documento'],
                nombre=datos['nombre'],
                apellido=datos['apellido'],
                sexo=datos['sexo'],
                nacimiento=datos['nacimiento'],
                u_consulta=datos['u_consulta'],
                medico=medico.numero_matricula 
            )

            paciente.save()

            return redirect('ListaInternados')
    
    else:
        form = FormularioInternados()

    return render(request, 'medicalapp/funciones/formInternado.html', {'form':form})


#--------------------------------------------------------------------------------------

#Editar info del paciente

@login_required
def editar_pacientes(request, pacienteDNI):
    paciente = Pacientes.objects.get(documento=pacienteDNI)

    if request.method == 'POST':
        form = FormularioPacientes(request.POST)

        if form.is_valid():

            datos = form.cleaned_data
            medico_numero_matricula = datos['medico']
            medico = Medicos.objects.get(numero_matricula=medico_numero_matricula)

            paciente = Pacientes(
                documento=datos['documento'],
                nombre=datos['nombre'],
                apellido=datos['apellido'],
                sexo=datos['sexo'],
                nacimiento=datos['nacimiento'],
                u_consulta=datos['u_consulta'],
                medico=medico.numero_matricula 
            )

            paciente.save()

            return redirect('ListaPacientes')
    else:
        form = FormularioPacientes(initial={'documento': paciente.documento, 'nombre': paciente.nombre, 'apellido': paciente.apellido,
                                                    'sexo': paciente.sexo, 'nacimiento': paciente.nacimiento, 'u_consulta': paciente.u_consulta, 'medico': paciente.medico})

    return render(request, 'medicalapp/funciones/paciente.html', {'form': form, 'documento': pacienteDNI})

#--------------------------------------------------------------------------------------

#Editar info del paciente en internacion

@login_required
def editar_internado(request, pacienteDNI):
    paciente = PacientesInternados.objects.get(documento=pacienteDNI)

    if request.method == 'POST':
        form = FormularioInternados(request.POST)

        if form.is_valid():

            datos = form.cleaned_data
            medico_numero_matricula = datos['medico']
            medico = Medicos.objects.get(numero_matricula=medico_numero_matricula)

            paciente = Pacientes(
                documento=datos['documento'],
                nombre=datos['nombre'],
                apellido=datos['apellido'],
                sexo=datos['sexo'],
                nacimiento=datos['nacimiento'],
                u_consulta=datos['u_consulta'],
                medico=medico.numero_matricula 
            )

            paciente.save()

            return redirect('ListaInternados')
    else:
        form = FormularioInternados(initial={'documento': paciente.documento, 'nombre': paciente.nombre, 'apellido': paciente.apellido,
                                                    'sexo': paciente.sexo, 'nacimiento': paciente.nacimiento, 'fecha_ingreso': paciente.fecha_ingreso, 'sala_asignada': paciente.sala_asignada, 'medico': paciente.medico})

    return render(request, 'medicalapp/funciones/pacienteinternado.html', {'form': form, 'documento': pacienteDNI})

#--------------------------------------------------------------------------------------

# Agregar campos faltantes al perfil de Medico

@login_required
def editar_medico(request, medico_id):
    medico = Medicos.objects.get(numero_matricula=medico_id)

    if request.method == 'POST':
        form = EdicionMedico(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('ListaMedicos')

    else:
        form = EdicionMedico(instance=medico)

    return render(request, 'medicalapp/funciones/editarMedico.html', {'form': form, 'medico': medico})

#--------------------------------------------------------------------------------------

