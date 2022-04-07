from django.urls import path
from Ruta.views import Cliente , Base , Pedido ,Movil, Inicio
urlpatterns = [
    path('', Inicio,name="Inicio") ,
    path('Cliente/', Cliente, name="Cliente") ,
    path('Base/', Base, name="Base") ,
    path('Pedido/', Pedido, name="Pedido") ,
    path('Movil/', Movil, name="Movil")
]