from django.shortcuts import render, redirect

# Create your views here.
from Persona.models import Persona


def mostrar(request):




    return render(request, "Persona/index.html")



def guardar(request):
    persona = Persona.objects.create(nombre="Valeria", apellido="Peruchi", edad=30)
    return redirect("Mostrar")
