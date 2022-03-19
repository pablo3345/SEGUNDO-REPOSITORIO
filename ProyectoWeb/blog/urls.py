from django.urls import path
from . import views  #from raiz me importas la views


urlpatterns = [



    path('', views.blog, name="Blog"), # vacio porque apunta a la raiz
    path('categoria/<int:categoria_id>/', views.categoria, name = "categoria") # va int porque el id en la base de datos es un int y aca lo toma como string



]
