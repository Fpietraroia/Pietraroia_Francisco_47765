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
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    avatar = forms.ImageField(label="Avatar", required=False)  

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2", "avatar"]

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
        medico = forms.ChoiceField(choices=[])

        def __init__(self, *args, **kwargs):
            super(FormularioPacientes, self).__init__(*args, **kwargs)
            medicos = Medicos.objects.all()
            choices = [(str(m.numero_matricula), str(m.numero_matricula)) for m in medicos]
            self.fields['medico'].choices = choices

#--------------------------------------------------------------------------------------

class FormularioInternados(forms.Form):
        documento = forms.IntegerField()
        nombre = forms.CharField(max_length=60)
        apellido = forms.CharField(max_length=60)
        sexo = forms.CharField(max_length=60)
        nacimiento = forms.DateField()
        fecha_ingreso = forms.DateField()
        sala_asignada = forms.CharField()
        medico = forms.ChoiceField(choices=[])

        def __init__(self, *args, **kwargs):
            super(FormularioPacientes, self).__init__(*args, **kwargs)
            medicos = Medicos.objects.all()
            choices = [(str(m.numero_matricula), str(m.numero_matricula)) for m in medicos]
            self.fields['medico'].choices = choices

#--------------------------------------------------------------------------------------

class EdicionMedico(forms.ModelForm):
    class Meta:
        model = Medicos
        fields = ['hospital', 'rama']

    def __init__(self, *args, **kwargs):
        super(EdicionMedico, self).__init__(*args, **kwargs)

        self.fields['hospital'] = forms.ModelChoiceField(
            queryset=Hospitales.objects.all(),
            empty_label="Seleccione un hospital",
            widget=forms.Select(attrs={'class': 'form-control'})
        )

        self.fields['rama'] = forms.ChoiceField(
            choices=RAMA_CHOICES,
            widget=forms.Select(attrs={'class': 'form-control'})
        )

# Forms de busqueda para la lista de pacientes -----------------------------------------------------

class BusquedaDNI(forms.Form):
    dni = forms.CharField(label= "Buscar por numero de documento: ")

class BusquedaDoc(forms.Form):
    doc = forms.CharField(label= "Buscar por numero de matricula: ")

class BusquedaSala(forms.Form):
    sala = forms.CharField(label= "Buscar por sala: ")

class BusquedaId(forms.Form):
    id = forms.CharField(label= "Buscar por ID de Hospital: ")

class BusquedaLocalidad(forms.Form):
    localidad = forms.CharField(label= "Buscar por Localidad: ")

# Formulario para el avatar ------------------------------------------------------------

class AvatarForm(forms.ModelForm):
     
     class Meta:
          model = Avatar
          fields = ["imagen"]

#--------------------------------------------------------------------------------------

