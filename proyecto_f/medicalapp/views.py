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
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            form.save()
            return render(request, 'medicalapp/inicio.html', {'mensaje':'Usuario Creado!'})
            
    else:
        form = RegistrationForm()
    return render(request, 'medicalapp/register.html', {'form': form})

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
        
    return render(request, "medicalapp/login.html", {"form": form,})
    
   
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
    return render(request, "medicalapp/editarUsuario.html", {'form':form , 'usuario':usuario})

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

    return render(request, "medicalapp/agregarAvatar.html", {"form":form})


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

    return render(request, 'medicalapp/listaPacientes.html', {'form_dni' : form_dni , 'form_doc' : form_doc , 'pacientes': pacientes})

#--------------------------------------------------------------------------------------

#Vista de pacientes

@login_required
def paciente(request, paciente_id):
    paciente = get_object_or_404(Pacientes, pk=paciente_id)
    return render(request, 'medicalapp/paciente.html', {'paciente': paciente})

#--------------------------------------------------------------------------------------

#Eliminar Paciente

@login_required
def eliminar_paciente(request, pacienteDNI):
     paciente = Pacientes.objects.get(documento=pacienteDNI)
     paciente.delete()

     pacientes = Pacientes.objects.all()

     return render(request, 'medicalapp/listaPacientes.html', {'pacientes' : pacientes, 'documento':pacienteDNI})

#--------------------------------------------------------------------------------------

#Agregar un paciente a la BD

@login_required
def agregar_paciente(request):
    if request.method == 'POST':

        miformulario = FormularioPacientes(request.POST)

        if miformulario.is_valid():

            datos = miformulario.cleaned_data

            paciente = Pacientes(documento=datos['documento'], nombre=datos['nombre'], apellido=datos['apellido'], sexo=datos['sexo'], nacimiento=datos['nacimiento'], u_consulta=datos['u_consulta'], medico=datos['medico'])

            paciente.save()

            mensaje = "Paciente ingresado con exito!"

            return render(request, 'medicalapp/inicio.html', {"mensaje":mensaje})
    
    else:
        miformulario = FormularioPacientes()

    return render(request, 'medicalapp/formPacientes.html', {'miformulario':miformulario})

#--------------------------------------------------------------------------------------

#Editar info del paciente

@login_required
def editar_pacientes(request, pacienteDNI):
    paciente = Pacientes.objects.get(documento=pacienteDNI)

    if request.method == 'POST':
        miformulario = FormularioPacientes(request.POST)

        if miformulario.is_valid():
            datos = miformulario.cleaned_data

            paciente.documento = datos['documento']
            paciente.nombre = datos['nombre']
            paciente.apellido = datos['apellido']
            paciente.sexo = datos['sexo']
            paciente.nacimiento = datos['nacimiento']
            paciente.u_consulta = datos['u_consulta']
            paciente.medico = datos['medico']

            paciente.save()

            return redirect('Listapacientes')
    else:
        miformulario = FormularioPacientes(initial={'documento': paciente.documento, 'nombre': paciente.nombre, 'apellido': paciente.apellido,
                                                    'sexo': paciente.sexo, 'nacimiento': paciente.nacimiento, 'u_consulta': paciente.u_consulta, 'medico': paciente.medico})

    return render(request, 'medicalapp/paciente.html', {'miformulario': miformulario, 'documento': pacienteDNI})