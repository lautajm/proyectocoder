
from django import forms

class Clienteformulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    Contacto= forms.IntegerField()
    pedido=forms.IntegerField()
    cliente=forms.IntegerField()
    domicilio=forms.CharField(max_length=50)

class Movilformulario(forms.Form):
    Nombre=forms.CharField(max_length=50)
    Apellido=forms.CharField(max_length=50)
    Legajo=forms.IntegerField()
    Tipo=forms.IntegerField()
    Estado=forms.BooleanField()

class Pedidoformulario(forms.Form):
    Numero=forms.IntegerField()
    Estado=forms.BooleanField()

