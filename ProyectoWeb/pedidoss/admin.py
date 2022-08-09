from django.contrib import admin
from .models import Pedido, LineaPedido

# Register your models here.

admin.site.register([Pedido, LineaPedido]) # hacemos esto para que me aparezcan en el panel de adm. , [] lo que aparece aca adentro es una lista
