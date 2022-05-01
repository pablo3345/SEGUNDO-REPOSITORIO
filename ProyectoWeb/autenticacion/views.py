from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.


class VRegistro(View): # una clase que se transforma en vista
   def get(self, request): # el get es para ofrecernos el formulario es lo que renderice el formulario, ahora le tenemos que decir que renderice el formulario para verlo y lo hacemos en la funcion get que es la encargada de mostrarlo
      form= UserCreationForm # form viene de formulario
      return render(request, "registro/registro.html", {"form": form}) # ponemos la ruta para que busque el html

   def post(self, request): # el post es el encargado de enviar los datos a la base de datos
      form= UserCreationForm(request.POST)#request es la peticion y POST es todos los datos que estamos enviando como el usuario y la contraseña

      if form.is_valid(): # por si no me marca error al crear la contraseña, osea si no respeto lo que dice el formulario de autenticacion
        usuario = form.save() #creamos una variable usuario, donde se va a almacenar la informacion del formulario, con esto save() se almacenan los datos en la base de datos de usuarios

        login(request, usuario) # una vez que lo guardo en la base de datos, quiero que el usuario este logeado
        return redirect('Home') # nos redirecciona a la url home

      else:
         for msg in form.error_messages: # un for para recorrer los errores que haya en el formulario
             messages.error(request, form.error_messages[msg]) #esto es para mostrarme ese error, [msg] esto es porque es un array de errores, msg para mostrar la ubicacion del error en concreto

         return render(request, "registro/registro.html", {"form": form}) # para que me muestre el formulario con los errores, esta fuera del for




def cerrar_sesion(request): #una nueva vista
    logout(request)
    return redirect('Home')


def logear(request):

    if request.method == "POST": # si ha apretado el boton, si hizo un post
        form = AuthenticationForm(request, data=request.POST) # aca en form me guarda los datos del formulario con los datos
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username") #dame la informacion que tengo guardado en el cuadro de texto que por defecto se llama "usurname"
            contraseniaa = form.cleaned_data.get("password")
            usuario = authenticate(username= nombre_usuario, password = contraseniaa) # la forma de autenticar el usuario
            if usuario is not None: # si hay algo como un usuario y contraseña,  entonces me haces un login
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request, "usuario no valido") # si no hay usuario entonce me pones este mensaje
        else:
            messages.error(request, "informacion incorrecta")  # este else viene de arriba, si el usuario no ha ingresado los datos correctamente




    form = AuthenticationForm() # con esto ya tenemos en form el formulario de login
    return render(request, "login/login.html", {"form": form}) # esta dos lineas de codigo es x si el usuario no le da al boton de logear, si no hace un post
