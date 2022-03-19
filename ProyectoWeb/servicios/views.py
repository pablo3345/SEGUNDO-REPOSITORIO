from django.shortcuts import render
from servicios.models import servicio

# Create your views here.


def servicios(request):
    servicios = servicio.objects.all() # con esto le digo que importe todos los objetos que tengo en la clase "servicio"
    return render(request, "servicios/servicios.html", {"servicios": servicios})