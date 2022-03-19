from django.urls import path

from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [

    path('', views.home, name= "Home"), #parece que dejandolo en blanco a esta url se ejecuta sola en el buscador, es la pagina de inicio






]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #para las imagenes (media)