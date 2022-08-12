from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.html import strip_tags

from carro.carro import Carro
from pedidoss.models import Pedido, LineaPedido
from django.contrib import messages
from django.template.loader import render_to_string

#@login_required(login_url="autenticacion/logear") #especificamos la url de logear por si el usuario no esta logeado y quiera acceder entonces este decorador lo lleva a la url de logear, esto es si el carro aparece siempre visible
def procesar_pedido(request):

    pedido= Pedido.objects.create(user=request.user) # esto es el usuario que esta dando de alta este pedido
    carro=Carro(request) # con esto ya tengo el carro para recorrerlo con un for

    lineas_pedidos = list() # creo una lista para poder almacenar esos items del carro por ejemplo los productos y la cantidad

    for key, value in carro.carro.items(): # para recorrer el carro x cada clave valor de los items del carro lo agregamos a la lista lineas_pedidos y por eso llamo al modelo LineaPedido
        lineas_pedidos.append(LineaPedido(

            producto_id = key, #la clave key seria igual al id del pedido,,,,producto_id fijarse en el modelo xq en LineaPedido juan lo corrigio a pedido (pero parece que funciona lo mismo)
            cantidad = value['cantidad'],
            user= request.user, #necesito meter tambien el usuario
            pedido=pedido # tambien metemos el pedido


        ))

    LineaPedido.objects.bulk_create(lineas_pedidos) # con esto guardamos la lista en la BBDD, LineaPedido que es el modelo, con bulk_create seria como muchos insert into en la BBDD

    enviar_mail(pedido=pedido,
                lineas_pedidos=lineas_pedidos,
                nombreusuario = request.user.username,
                emailusuario = request.user.email


                    )


    messages.success(request, "El pedido se ha realizado correctamente")


    return redirect("../tienda")



def enviar_mail(**kwargs):


   asunto = "Gracias por el pedido"
   mensaje= render_to_string("emails/pedido.html", {

       "pedido": kwargs.get("pedido"),
       "lineas_pedidos": kwargs.get("lineas_pedidos"),
       "nombreusuario": kwargs.get("nombreusuario")





   }) # aca vamos a guardar todas las lineas de pedido como lineas pedidos de arriba, con render_to_string le decimos que renderice el siguiente html

   mensaje_texto=strip_tags(mensaje) # esto va a ser igual a la variable mensaje que creamos arriba donde hemos renderizado toda la informacion, pero ignorando toda etiqueta html como esta<> lo hacemos con strip_tags, le decimos que ignore las etiquetas html de la variable mensaje

   from_mail="pabloandresperuchi@gmail.com" # de quien es el correo electronico, el de la tienda
   #to=  kwargs.get("emailusuario")# el destinatario de los correos, con kwargs.get() obtengo los parametros de la funcion de arriba que le pase enviar_mail(), como no puse ningun usuario con un correo valido a esto lo comento y pongo mi correo personal
   to= "sumerx21@yahoo.com.ar"



   #ahora entra la funcion send_mail para enviar el mail

   send_mail(asunto, mensaje_texto, from_mail, [to], html_message=mensaje) #mensaje texto es el mensaje sin etiquetas html, cuando enviamos un mensaje html debemos especificarlo con html_message=


