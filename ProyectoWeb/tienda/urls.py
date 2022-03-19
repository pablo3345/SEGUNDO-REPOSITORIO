from django.urls import path

from ProyectoWebApp import views
from . import views     #para importar las vistas





urlpatterns = [


    path('', views.tienda, name="Tienda"),





]

