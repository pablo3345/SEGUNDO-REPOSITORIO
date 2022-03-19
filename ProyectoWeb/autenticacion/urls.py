from django.urls import path



from .views import VRegistro


urlpatterns = [



    path('', VRegistro.as_view(), name="Autenticacion"), # es_view es para que nos muestre esta clase como una vista



]
