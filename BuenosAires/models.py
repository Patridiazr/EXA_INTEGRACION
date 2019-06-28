
from django.db import models

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    contra = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=30)
    comuna = models.CharField(max_length=100)

class Solicitud(models.Model):
    nombres = models.CharField(max_length=100)
    direccion = models.CharField( default="default" ,max_length=100)
    email = models.EmailField(max_length=100)
    asunto = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=100)
    estado = models.CharField(default="Pendient",max_length=10, null="true")

class ProduI(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

class Producto(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField(default="0")