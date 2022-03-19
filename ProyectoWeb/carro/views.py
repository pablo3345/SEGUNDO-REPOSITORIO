from django.shortcuts import render
from .carro import Carro
from tienda.models import Producto #el modelo de Producto estaba dentro de la aplicacion tienda
from django.shortcuts import redirect # vamos hacer redirecciones, cada vez que agreguemos un producto al carro, vaciamos, eliminamos etc debemos redireccionar a la pagina de la tienda para que refleje los cambios que hemos hecho en el carro


# Create your views here.

def agregar_producto(request, producto_id):
    carro = Carro(request) # creamos el carro
    producto = Producto.objects.get(id= producto_id)  #obtener el producto que vamos a agregar al carro con el id
    carro.agregarProducto(producto= producto) # ahora agregamos el producto llamando a la clase carro agregarProducto

    return redirect("Tienda") # redireccionamos a la url "tienda" que ya creamos antes en videos atras



def eliminar_producto(request, producto_id):
    carro = Carro(request) # creamos el carro
    producto = Producto.objects.get(id= producto_id)
    carro.eliminar(producto= producto)


    return redirect("Tienda") # redireccionamos a la url "tienda" que ya creamos antes en videos atras



def restar_producto(request, producto_id):
    carro = Carro(request) # creamos el carro
    producto = Producto.objects.get(id= producto_id)
    carro.restar_producto(producto= producto)

    return redirect("Tienda") # redireccionamos a la url "tienda" que ya creamos antes en videos atras



def limpiar_carro(request):
    carro = Carro(request) # creamos el carro

    carro.limpiar_carro()

    return redirect("Tienda") # redireccionamos a la url "tienda" que ya creamos antes en videos atras