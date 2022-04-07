from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.

def Cliente(request):

    return render(request, "Ruta/Cliente.html", )

def Pedido(request):

    return render(request, "Ruta/Pedido.html")
def Base(request):

    return render(request, "Ruta/Base.html")
def Movil(request):

    return render(request, "Ruta/Movil.html")

def Inicio(request):

    return render(request, "Ruta/Inicio.html")