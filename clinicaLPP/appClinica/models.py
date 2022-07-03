from django.db import models

class personal(models.Model):                        
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    cargo = models.CharField(max_length=20)
    dni = models.IntegerField()
    def __str__(self) -> str:
        return self.nombre +" "+ self.apellido + ": " + self.cargo

class paciente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField()
    obra_social= models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombre +" "+ self.apellido + " Obra social: " + self.obra_social

class solicitud_turno(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=40)
    email = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.apellido + " Solicita turno para: " + self.especialidad
    
