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

class PacientesInternados(models.Model):

        def __str__(self):
               return f"Nombre: {self.nombre} --- DNI:{self.documento}"
               
        documento = models.IntegerField(primary_key=True)
        nombre = models.CharField(max_length=60)
        apellido = models.CharField(max_length=60)
        sexo = models.CharField(max_length=60)
        nacimiento = models.DateField()
        fecha_ingreso = models.DateField()
        sala_asignada = models.CharField(max_length=60, default = "1A")
        medico = models.CharField(max_length=60)

#--------------------------------------------------------------------------------------

class Hospitales(models.Model):

        def __str__(self):
               return f"Nombre: {self.nombre} --- ID:{self.id}"
               
        id = models.IntegerField(primary_key=True)
        nombre = models.CharField(max_length=60)
        direccion = models.CharField(max_length=60)
        localidad = models.CharField(max_length=60)

#--------------------------------------------------------------------------------------

class Medicos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospitales, on_delete=models.SET_NULL, null=True, blank=True)  
    rama_choices = (
        ('Traumatologo', 'Traumatologo'),
        ('Oftalmologo', 'Oftalmologo'),
        ('Enfermero', 'Enfermero'),
        ('Cirujano', 'Cirujano'),
    )
    rama = models.CharField(max_length=20, choices=rama_choices)
    numero_matricula = models.AutoField(primary_key=True)

    def __str__(self):
        return self.user.username
    
def save(self, *args, **kwargs):
        if self.numero_matricula is None:
            last_medico = Medicos.objects.order_by('-numero_matricula').first()
            if last_medico:
                self.numero_matricula = last_medico.numero_matricula + 1
            else:
                self.numero_matricula = 123456
        super(Medicos, self).save(*args, **kwargs)
        
#--------------------------------------------------------------------------------------

class Avatar(models.Model):
        usuario = models.ForeignKey(User, on_delete=models.CASCADE)
        imagen = models.ImageField(upload_to= "avatares", null=True, blank=True)

#--------------------------------------------------------------------------------------

RAMA_CHOICES = (
    ('Traumatologo', 'Traumatologo'),
        ('Oftalmologo', 'Oftalmologo'),
        ('Enfermero', 'Enfermero'),
        ('Cirujano', 'Cirujano'),
)