from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [


    path('', views.servicios, name="Servicios"), # name= "Servicios " es el nombre que le pusimos a las url
    # es '' porque apunta a la raiz 127.0.0.1: 8000





]
