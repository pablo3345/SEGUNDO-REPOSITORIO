from django.shortcuts import render

# Create your views here.
from Persona.models import Persona


def guardarPersona(request):
    persona = Persona.objects.create(nombre="Maria", apellido="emilia", edad=30)



    return render(request, "Persona/index.html")
