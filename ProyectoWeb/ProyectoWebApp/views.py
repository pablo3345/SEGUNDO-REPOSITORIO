from django.shortcuts import render, HttpResponse



# Create your views here.
from carro.carro import Carro


def home(request):
    carro=Carro(request)#como me marcaba error key carro lo que hice con esto que al comenzar la aplicacion ya me inicia el carro, y este carro ya esta disponible para toda la aplicacion


    return render(request, "ProyectoWebApp/home.html")









