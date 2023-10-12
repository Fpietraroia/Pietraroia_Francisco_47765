from django.urls import path
from medicalapp.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('registrarse/', registro, name="Registrarse"),
    path('login/', iniciosesion, name="Login"),
    path('agregar_avatar', agregarAvatar, name="AgregarAvatar"),
    path('sobre_mi', sobremi, name="SobreMi"),
    path('logout/', LogoutView.as_view(template_name="medicalapp/users/logout.html"), name="Logout"),
    path('editar_usuario/', editar_usuario, name="EditarUsuario"),
    path('lista_pacientes/', lista_pacientes, name="ListaPacientes"),
    path('lista_internados/', lista_internados, name="ListaInternados"),
    path('lista_hospitales/', lista_hospitales, name="ListaHospitales"),
    path('lista_medicos/', lista_medicos, name="ListaMedicos"),

    
    
    #CRUD
    path('eliminar_paciente/<pacienteDNI>/', eliminar_paciente, name="EliminarPaciente"),
    path('eliminar_internado/<pacienteDNI>/', eliminar_internado, name="EliminarInternado"),
    path('detalle_paciente/<pacienteDNI>/', editar_pacientes, name="DetallePacientes"),
    path('detalle_internado/<pacienteDNI>/', editar_internado, name="DetalleInternado"),
    path('agregar_medico/<medico_id>/', editar_medico, name="EditarMedico"),
    path('agregar_paciente/', agregar_paciente, name="AgregarPaciente"),
    path('agregar_internado/', agregar_internado, name="AgregarInternado"),

    ]

