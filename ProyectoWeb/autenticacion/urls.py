from django.urls import path



from .views import VRegistro, cerrar_sesion, logear


urlpatterns = [



    path('', VRegistro.as_view(), name="Autenticacion"), # es_view es para que nos muestre esta clase como una vista
    path('cerrar_sesion', cerrar_sesion, name="Cerrar_sesion"),
    path('logear', logear, name="Logear"),



]
