from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
# Create your views here.


def contacto(request):
    formulario_Contacto = FormularioContacto()

    if request.method =="POST": #si se ha hecho POST tiene que rescatar la informacion que esta en el formulario
        formulario_Contacto = FormularioContacto(data=request.POST) #aca lo que hicimos es cargar en el formulario la informacion que ha ido introduciendo en el formulario (esto lo hago con date=request.POST)
        if formulario_Contacto.is_valid(): #si el formulario es valido me vas a guardar en las variable lo que tenemos almacenado

            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email=EmailMessage("Mensaje desde app Django ProyectoWeb", # el asunto del correo cuando lo recibo
            "El usuario con nombre {} con direccion {} escribe lo siguiente:\n\n {}".format(nombre, email, contenido), "", ["pabloandresperuchi@gmail.com"], reply_to=[email]) # las "" no pongo nada xq ya se que el mail viene de la aplicacion, el reply_to significa que puedo responderle al correo que me envian

            try:
                email.send() # creiria que este email se relaciona solo con email=EmailMessage, los otros email deben ser del formulario
                return redirect("/contacto/?valido") #le paso por parametro la palabra valido en la url para hacer un if en el html con la palabra valido, y me aparezca el mensaje que la informacion se envio correctamente


            except:

                return redirect("/contacto/?noValido")



    return render(request, "contacto/contacto.html", {'miFormulario': formulario_Contacto}) # ahora le paso como parametro el diccionario