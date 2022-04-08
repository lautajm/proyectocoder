from django import http
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

def clienteformulario(request):
    if request.method =="POST":
        miFormulario=Clienteformulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cliente=Cliente (nombre=informacion["nombre"] ,apellido=informacion["apellido"],contacto=informacion["contacto"],pedido=informacion["pedido"],cliente=informacion["nro_de_cliente"],domicilio=informacion["domicilio"])
            cliente.save()
        return render(request, 'Ruta/Inicio.html')
    else:
        miFormulario= Clienteformulario()
    return render(request, "Ruta/Clienteformulario.html",{"miFormulario":miFormulario})

def pedidoformulario(request):
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


def movilformulario(request):
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

def busquedaMovil(request):

    return render(request, "Ruta/busquedaMovil.html")

def busquedaCliente(request):

    return render(request, "Ruta/busquedaCliente.html")

def busquedaPedido(request):
    return render(request, "Ruta/busquedaPedido.html")

def BuscarM(request):
    if request.GET["legajo"]:
        legajo=request.GET["legajo"]
        matricula=Movil.objects.filter(legajo=legajo)

        return render(request, "Ruta/Movil.html", {"legajo":legajo, "matricula":matricula})
    else:
        return HttpResponse(f"No enviaste el legajo del chofer")

def BuscarC(request):
    if request.GET["nro de cliente"]:
        nro_de_cliente=request.GET["nro_de_cliente"]
        pedido=Cliente.objects.filter(nro_de_cliente=nro_de_cliente)

        return render(request, "Ruta/Cliente.html", {"nro_de_cliente":nro_de_cliente, "pedido":pedido})
    else:
        return HttpResponse(f"No enviaste el numero del cliente")

def BuscarP(request):
    if request.GET["nro de cliente"]:
        numero=request.GET["numero"]
        Estado=Cliente.objects.filter(numero=numero)

        return render(request, "Ruta/Pedido.html", {"numero":numero, "Estado":Estado})
    else:
        return HttpResponse(f"No enviaste el numero del pedido")