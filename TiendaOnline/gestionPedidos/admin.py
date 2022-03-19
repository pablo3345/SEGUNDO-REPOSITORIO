from django.contrib import admin

from gestionPedidos.models import Cliente, Articulos, Pedidos #importamos el modelo

# Register your models here.

class ClientesAdmin(admin.ModelAdmin): # va a heredear de MdelAdmin, por lo que recibe por parametro

    list_display = ("nombre", "direccion", "telefono")# estos son los nombres que quiero que me aparezcan en las columnas del panel de adm.
    search_fields = ("nombre", "telefono")#con esto es un casillero de busqueda en el panel y me va a buscar por nombre y telefono, lo ideal seria que me busque por apellido

class ArticulosAdmin(admin.ModelAdmin):
    list_filter = ("seccion",)# para hacer un filtro en el panel de adm. y me traiga por seccion

class PedidosAdmin(admin.ModelAdmin):
    list_display = ("numero", "fecha", "entregado")
    list_filter = ("fecha",)
    date_hierarchy = "fecha" # para que arriba del panel me aparezca para traer cada mes de los pedidos

admin.site.register(Cliente, ClientesAdmin) #esto es para que desde el panel de administracion tengamos disponible la tabla de Cliente etc
                                            # y tambien va a heredar la clase de arriba
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
