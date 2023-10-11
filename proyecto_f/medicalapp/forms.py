from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from django.contrib.auth.models import 
from medicalapp.models import *

#--------------------------------------------------------------------------------------

class RegistrationForm(UserCreationForm):
   first_name = forms.CharField(label="Nombre")
   last_name = forms.CharField(label="Apellido")
   email = forms.EmailField()
   password1 = forms.CharField(label="Contraseña: ", widget=forms.PasswordInput)
   password2 = forms.CharField(label="Repetir Contraseña: ", widget=forms.PasswordInput)
   
   class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
   def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Nombre de usuario"

#--------------------------------------------------------------------------------------

class EditarUsuario(UserCreationForm):
   first_name = forms.CharField(label="Nombre")
   last_name = forms.CharField(label="Apellido")
   email = forms.EmailField()
   password1 = forms.CharField(label="Contraseña: ", widget=forms.PasswordInput)
   password2 = forms.CharField(label="Repetir Contraseña: ", widget=forms.PasswordInput)
   
   class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]

#--------------------------------------------------------------------------------------

class FormularioPacientes(forms.Form):
        documento = forms.IntegerField()
        nombre = forms.CharField(max_length=60)
        apellido = forms.CharField(max_length=60)
        sexo = forms.CharField(max_length=60)
        nacimiento = forms.DateField()
        u_consulta = forms.DateField()
        medico = forms.CharField(max_length=60)

# Forms de busqueda para la lista -----------------------------------------------------

class BusquedaDNI(forms.Form):
    dni = forms.CharField(label= "Buscar por numero de documento: ")

class BusquedaDoc(forms.Form):
    doc = forms.CharField(label= "Buscar por numero de matricula: ")

# Formulario para el avatar ------------------------------------------------------------

class AvatarForm(forms.ModelForm):
     
     class Meta:
          model = Avatar
          fields = ["imagen"]