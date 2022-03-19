from django.urls import path

from ProyectoWebApp import views
from . import views     #para importar las vistas



app_name="carro" #sirve para que no haya coalisiones cuando tengo url parecidas,  con poner antes carro y luego agregar, eliminar, restar etc etc (lo que dice en name="")

urlpatterns = [


    path('agregar/<int:producto_id>/', views.agregar_producto, name = "agregar"), #agregamos el id del producto que queremos agregar (producto_id es el id que tenemos identificado en el diccionario de agregarProducto por ejemplo)
    path("eliminar/<int:producto_id>/", views.eliminar_producto, name = "eliminar"),
    path("restar/<int:producto_id>/", views.restar_producto, name = "restar"),
    path("limpiar/", views.limpiar_carro, name = "limpiar"),




]

