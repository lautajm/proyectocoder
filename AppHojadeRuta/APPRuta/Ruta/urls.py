from django.urls import path
from .views import BuscarC, BuscarM, BuscarP, Cliente , Base , Pedido ,Movil, Inicio, clienteformulario, movilformulario,pedidoformulario,busquedaPedido,busquedaCliente,busquedaMovil


urlpatterns = [
    path('', Inicio,name="Inicio") ,
    path('Cliente/', Cliente, name="Cliente") ,
    path('Base/', Base, name="Base") ,
    path('Pedido/', Pedido, name="Pedido") ,
    path('Movil/', Movil, name="Movil"),
    path('Clienteformulario/', clienteformulario, name="Clienteformulario"),
    path('Movilformulario/', movilformulario, name="Movilformulario"),
    path('Pedidoformulario/', pedidoformulario, name="Pedidoformulario"),
    path('Movil/', Movil, name="Movil"),
    path('busquedaMovil/', busquedaMovil, name="busquedaMovil"),
    path('busquedaCliente/', busquedaCliente, name="busquedaCliente"),
    path('busquedaPedido/', busquedaPedido, name="busquedaPedido"),
    path('buscarM/', BuscarM),
    path('buscarC/', BuscarC),
    path('buscarP/', BuscarP),
    ]