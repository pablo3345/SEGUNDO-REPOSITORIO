from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.

from carro.carro import Carro
from pedidoss.models import Pedido, LineaPedido
from django.contrib import messages

#@login_required(login_url="autenticacion/logear") #especificamos la url de logear por si el usuario no esta logeado y quiera acceder entonces este decorador lo lleva a la url de logear, esto es si el carro aparece siempre visible
def procesar_pedido(request):

    pedido= Pedido.objects.create(user=request.user) # esto es el usuario que esta dando de alta este pedido
    carro=Carro(request) # con esto ya tengo el carro para recorrerlo con un for

    lineas_pedidos = list() # creo una lista para poder almacenar esos items del carro por ejemplo los productos y la cantidad

    for key, value in carro.carro.items(): # para recorrer el carro x cada clave valor de los items del carro lo agregamos a la lista lineas_pedidos y por eso llamo al modelo LineaPedido
        lineas_pedidos.append(LineaPedido(

            producto_id = key, #la clave key seria igual al id del pedido
            cantidad = value['cantidad'],
            user= request.user, #necesito meter tambien el usuario
            pedido=pedido # tambien metemos el pedido


        ))

    LineaPedido.objects.bulk_create(lineas_pedidos) # con esto guardamos la lista en la BBDD, LineaPedido que es el modelo, con bulk_create seria como muchos insert into en la BBDD

        #enviar_mail(pedido=pedido,
         #           lineas_pedidos=lineas_pedidos,
          #          nombreusuario = request.username,
           #         emailusuario = request.usermail


                 #   )


    messages.success(request, "El pedido se ha realizado correctamente")


    return redirect("../tienda")



#def enviar_mail(**kwargs):


 #  asunto = "Gracias por el pedido"
