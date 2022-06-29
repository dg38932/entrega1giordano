from django.db import models

# Create your models here.

Turnos = (('mañana', "MAÑANA"),('tarde',"TARDE"))

class Empleados(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    turno = models.CharField(max_length=6, choices=Turnos)
    fechaIngreso = models.DateField()


class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Productos(models.Model):
    descripcion = models.CharField(max_length=40)
    codigo = models.IntegerField()
    stock = models.IntegerField()