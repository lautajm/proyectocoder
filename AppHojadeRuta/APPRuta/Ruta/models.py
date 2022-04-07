
from django.db import models

# from django.utils import timezone
# from django.conf import settings

# Create your models here.

# class Pedido(models.Model):
#     id = models.IntegerField("id")
#     Estado = models.CharField("Estado",max_length=50)
#     # Hora_de_creacion=models.DateTimeField(
#     #     default=timezone.now)
#     Estimado= models.CharField("Estimado",max_length=50)
#Intento con 3 modelos primero

class Movil(models.Model):
    Estado = models.CharField("Estado",max_length=50)
    Tipo = models.IntegerField("Tipo")#camioneta/camion/auto
    Matricula = models.CharField("Matricula",max_length=50)
    nombre=models.CharField("nombre",max_length=50)
    apellido=models.CharField("apellido",max_length=50)

class Cliente(models.Model):
    pedido = models.IntegerField()#(pedido)
    direccion=models.CharField("Direccion",max_length=50)
    Contacto=models.CharField("Contacto",max_length=50)
    nombre=models.CharField("nombre",max_length=50)
    apellido=models.CharField("apellido",max_length=50)

class Base(models.Model):
    Estado=models.CharField("Estado",max_length=50)
    Cant_moviles=models.CharField("CantidadMovil",max_length=50)
    Cant_pedidos=models.CharField("CantidadPedidos",max_length=50)
    Contacto=models.CharField("NumerodeContacto",max_length=50)

class Pedido(models.Model):
    numero=models.IntegerField()
    Estado=models.BooleanField()
    fechadeentrega=models.DateField()