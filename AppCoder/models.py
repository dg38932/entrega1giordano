from django.db import models

# Create your models here.

class Empleados(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fechaIngreso = models.DateField()


class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

class Productos(models.Model):
    descripcion = models.CharField(max_length=40)
    codigo = models.IntegerField()
    stock = models.IntegerField()