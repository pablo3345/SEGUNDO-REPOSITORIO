from django.shortcuts import render

from .models import Producto
# Create your views here.


def tienda(request):

    productos = Producto.objects.all() #con esto me trae todos los productos

    return render(request, "tienda/tienda.html", {"productos": productos})


