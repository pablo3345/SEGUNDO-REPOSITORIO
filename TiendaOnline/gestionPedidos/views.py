from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from  django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import FormularioDeContacto

# Create your views here.

def busqueda_productos(request):
    return render(request, "busqueda_productos.html")


def buscar(request): #la url de esta vista es la que le puse al boton del html en action para que la busque
    if request.GET["producto"]:# hacemos un if que controle si viene informacion del formulario, si esto es verdad me almacenas en la variable productoss , y si no es xq el usuario no ingreso nada en el cuadro de texto (para saber si no ingrese nada en el campo de texto)

      # mensaje = "Articulo buscado: %r" %request.GET["producto"] # primero hay que importar la libreria arriba Http y con GET obtengo lo que el
      # usuario  entro en el cuadro de texto del html

      productoss= request.GET["producto"] #producto es el campo de texto del input del html

      if len(productoss)>20: #la longitud de caracteres que ingresa el usuario, mayor a 20
          mensaje = "texto de busqueda demasiado largo"
      else:

          articulos =Articulos.objects.filter(nombre__icontains = productoss)# el icontains funciona colo un like en una consulta en sql
                                                                          # me va a traer todo lo que contenga la palabra raqueta por ejemplo
          return render(request, "resultados_busqueda.html", {"articulos": articulos, "consulta": productoss})



    else:
        mensaje= "No ha introducido ningun producto"

    return HttpResponse(mensaje) #objeto HttpResponse una respuesta

def contacto(request):


    if request.method =="POST": #si el usuario ha apretado el boton de enviar

      # subject = request.POST["asunto"] #que aca  me almacene lo que estaba en el input de contacto.html en "asunto"

     #  messaje = request.POST["mensaje"] + " " +request.POST["email"] #aca dejo un espacio en blanco y para que en el mensaje me aparezca el email del usuario

      # email_from = settings.EMAIL_HOST_USER #para especificar de que mail viene los correos ejemplo del que especifique del setting.py

      # recipient_list = ["sumerx21@yahoo.com.ar"] #la direccion donde quiero que lleguen los mensajes del formulario

     #  send_mail(subject, messaje, email_from, recipient_list) #email_from (de donde viene el mail), recipient_list (el destinatario)

      # return render(request, "gracias.html")

       miFormulario = FormularioDeContacto(request.POST) #para guardar la informacion del formulario al apretar el boton, al hacer POST, por eso se usa (request.POST)

       if miFormulario.is_valid(): #si mi formulario es valido devuelve True(osea a pasado la validacion), entonces tengo que hacer
          informacionFormulario = miFormulario.cleaned_data # cleaned_data nos marca las propiedades del formulario que son validas, nos dice cual es el asunto, el email y el mensaje,
                                                           # utilizamos cleaned_data para obtener esos campos del formulario que han sido enviadas

          send_mail(informacionFormulario['asunto'], informacionFormulario['mensaje']+ " " +request.POST["email"],
          informacionFormulario.get('El_email', 'pabloandresperuchi'),['sumerx21@yahoo.com.ar'],)# aca empiezo a pedir la informacion del formulario para que la envie al correo electronico

          return render(request, "gracias.html")


    else: #por si no envio el mail
            miFormulario = FormularioDeContacto() #por si no lo envio, un formulario vacio, xq todavia no ha apretado el boton enviar




    return render(request, "formulario_contacto.html", {'form': miFormulario}) #con form le indicamos que debe utilizar para construir el formulario
