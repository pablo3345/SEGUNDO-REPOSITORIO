from django.urls import path



from .import views


urlpatterns = [





   path('', views.mostrar, name="Mostrar"),
   path('guardar', views.guardar, name="Guardar"),



]