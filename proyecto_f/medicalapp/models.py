from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#--------------------------------------------------------------------------------------

class Pacientes(models.Model):

        def __str__(self):
               return f"Nombre: {self.nombre} --- DNI:{self.documento}"
               
        documento = models.IntegerField(primary_key=True)
        nombre = models.CharField(max_length=60)
        apellido = models.CharField(max_length=60)
        sexo = models.CharField(max_length=60)
        nacimiento = models.DateField()
        u_consulta = models.DateField()
        medico = models.CharField(max_length=60)

#--------------------------------------------------------------------------------------

class Avatar(models.Model):
        usuario = models.ForeignKey(User, on_delete=models.CASCADE)
        imagen = models.ImageField(upload_to= "avatares", null=True, blank=True)

#--------------------------------------------------------------------------------------

