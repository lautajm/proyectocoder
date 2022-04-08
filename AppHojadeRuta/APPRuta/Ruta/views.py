import re
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from Ruta.forms import Clienteformulario,Movilformulario,Pedidoformulario

# Create your views here.

def Cliente(request):

    return render(request, "Ruta/Cliente.html" )

def Pedido(request):

    return render(request, "Ruta/Pedido.html")
def Base(request):

    return render(request, "Ruta/Base.html")
def Movil(request):

    return render(request, "Ruta/Movil.html")

def Inicio(request):

    return render(request, "Ruta/Inicio.html")

def Clienteformulario(request):
    if request.method =="POST":
        miFormulario=Clienteformulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cliente=Cliente (nombre=informacion["nombre"] ,apellido=informacion["apellido"],contacto=informacion["nro de contacto"],pedido=["nro de pedido"],cliente=["nro de cliente"],domicilio=["domicilio"])
            cliente.save()
        return render(request, 'Ruta/Inicio.html')
    else:
        miFormulario= Clienteformulario()
    return render(request, "Ruta/Clienteformulario.html",{"miFormulario":miFormulario})

def Pedidoformulario(request):
    if request.method =="POST":
        miFormulario=Pedidoformulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            pedido=Pedido(numero=informacion["numero"] ,Estado=informacion["Estado"])
            pedido.save()
        return render(request, 'Ruta/Inicio.html')
    else:
        miFormulario= Pedidoformulario()
    return render(request, "Ruta/Pedidoformulario.html",{"miFormulario":miFormulario})


def Movilformulario(request):
    if request.method =="POST":
        miFormulario=Movilformulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            movil=Movil (nombre=informacion["nombre"] ,apellido=informacion["apellido"],matricula=informacion["nro de matricula"],legajo=["nro de legajo"],tipo=["tipo de automovil"],estado=["Estado"])
            movil.save()
        return render(request, 'Ruta/Inicio.html')
    else:
        miFormulario= Movilformulario()
    return render(request, "Ruta/Movilformulario.html",{"miFormulario":miFormulario})


