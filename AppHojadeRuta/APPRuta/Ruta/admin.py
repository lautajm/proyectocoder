from atexit import register
from django.contrib import admin

# Register your models here.
from .models import*

admin.site.register (Movil)
admin.site.register(Base)
admin.site.register(Cliente)
admin.site.register(Pedido)

