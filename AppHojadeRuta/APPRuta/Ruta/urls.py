from django.urls import path
from .views import Cliente , Base , Pedido ,Movil, Inicio, Clienteformulario, Movilformulario,Pedidoformulario


urlpatterns = [
    path('', Inicio,name="Inicio") ,
    path('Cliente/', Cliente, name="Cliente") ,
    path('Base/', Base, name="Base") ,
    path('Pedido/', Pedido, name="Pedido") ,
    path('Movil/', Movil, name="Movil"),
    path('Clienteformulario/', Clienteformulario, name="Clienteformulario"),
    path('Movilformulario/', Movilformulario, name="Movilformulario"),
    path('Pedidoformulario/', Pedidoformulario, name="Pedidoformulario"),
    ]