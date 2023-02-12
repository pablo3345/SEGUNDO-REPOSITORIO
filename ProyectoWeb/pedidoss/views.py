from urllib import request

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import DetailView





from django.template import RequestContext

# Create your views here.
from django.utils.html import strip_tags

from carro.carro import Carro
from pedidoss.models import Pedido, LineaPedido
from django.contrib import messages
from django.template.loader import render_to_string


#@login_required(login_url="autenticacion/logear") #especificamos la url de logear por si el usuario no esta logeado y quiera acceder entonces este decorador lo lleva a la url de logear, esto es si el carro aparece siempre visible
def procesar_pedido(request):

    pedido= Pedido.objects.create(user=request.user) # esto es el usuario que esta dando de alta este pedido, cuando llame a esta funcion se va a crear
    carro=Carro(request) # con esto ya tengo el carro para recorrerlo con un for


    total=0










    lineas_pedidos = list() # creo una lista para poder almacenar esos items del carro por ejemplo los productos y la cantidad

    for key, value in carro.carro.items(): # para recorrer el carro x cada clave valor de los items del carro lo agregamos a la lista lineas_pedidos y por eso llamo al modelo LineaPedido
        total = total + float(value["precio"]) #para que me aparezca el total en el mail
        lineas_pedidos.append(LineaPedido(

            producto_id = key, #la clave key seria igual al id del pedido,,,,producto_id fijarse en el modelo xq en LineaPedido juan lo corrigio a pedido (pero parece que funciona lo mismo)
            cantidad = value['cantidad'],
            user= request.user, #necesito meter tambien el usuario
            pedido=pedido, # tambien metemos el pedido




        ))

    LineaPedido.objects.bulk_create(lineas_pedidos) # con esto guardamos la lista en la BBDD, LineaPedido que es el modelo, con bulk_create seria como muchos insert into en la BBDD

    enviar_mail(pedido=pedido,
                lineas_pedidos=lineas_pedidos,
                nombreusuario = request.user.username,
                emailusuario = request.user.email,
                total=total







    )






    #messages.success(request, "El pedido se ha realizado correctamente")








    return redirect("../tienda/?valido")





def enviar_mail(**kwargs):

    # render_to_string es que me renderice en pedido.html estos datos
   asunto = "Gracias por el pedido"
   mensaje= render_to_string("emails/pedido.html",  {

       "pedido": kwargs.get("pedido"),
       "lineas_pedidos": kwargs.get("lineas_pedidos"),
       "nombreusuario": kwargs.get("nombreusuario"),
       "total":kwargs.get("total"),











   }) # aca vamos a guardar todas las lineas de pedido como lineas pedidos de arriba, con render_to_string le decimos que renderice el siguiente html

   mensaje_texto=strip_tags(mensaje) # esto va a ser igual a la variable mensaje que creamos arriba donde hemos renderizado toda la informacion, pero ignorando toda etiqueta html como esta<> lo hacemos con strip_tags, le decimos que ignore las etiquetas html de la variable mensaje

   from_mail="pabloandresperuchi@gmail.com" # de quien es el correo electronico, el de la tienda, el que los manda
   #to=  kwargs.get("emailusuario")# el destinatario de los correos, con kwargs.get() obtengo los parametros de la funcion de arriba que le pase enviar_mail(), como no puse ningun usuario con un correo valido a esto lo comento y pongo mi correo personal

   to= "sumerx21@yahoo.com.ar"
   to2= "pabloandresperuchi@gmail.com" # cuando quiero enviar a mas de un destinatario



   #ahora entra la funcion send_mail para enviar el mail

   send_mail(asunto, mensaje_texto, from_mail, [to, to2], html_message=mensaje) #mensaje texto es el mensaje sin etiquetas html, cuando enviamos un mensaje html debemos especificarlo con html_message=

# class mail(DetailView):
#     template_name = "pedido.html"
#
# def get_context_date(self, **kwargs):
#     importe_total_carro= super(mail, self).get_context_date(**kwargs)
#     importe_total_carro['publishers']=self.object.publishers.filter(is_active=True)
#     return importe_total_carro

