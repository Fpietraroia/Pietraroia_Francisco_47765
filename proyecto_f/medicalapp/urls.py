from django.urls import path
from medicalapp.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('registrarse/', registro, name="Registrarse"),
    path('login/', iniciosesion, name="Login"),
    path('agregar_avatar', agregarAvatar, name="AgregarAvatar"),
    path('sobre_mi', sobremi, name="SobreMi"),
    path('logout/', LogoutView.as_view(template_name="medicalapp/logout.html"), name="Logout"),
    path('editar_usuario/', editar_usuario, name="EditarUsuario"),
    path('lista_pacientes/', lista_pacientes, name="ListaPacientes"),

    
    
    #CRUD
    path('eliminar_paciente/<pacienteDNI>/', eliminar_paciente, name="EliminarPaciente"),
    path('detalle_paciente/<pacienteDNI>/', editar_pacientes, name="DetallePacientes"),
    path('agregar_paciente/', agregar_paciente, name="AgregarPaciente"),
    ]

