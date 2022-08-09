from django.db import models

from django.contrib.auth import get_user_model


# Create your models here.
from tienda.models import Producto
from django.db.models import F, Sum, FloatField

User = get_user_model() # nos va a devolver el usuario que esta logeado, el usauario activo

class Pedido(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE) # es foreign key significa que si borro un usuario de este pedido tambien me va a borrar los registros de este usuario en la tabla de abajo LineaPadido, capaz es si borro un usuario en la tabla usuarios como esta como foreign key en estos dos modelos
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.id  #que me devuelva el id del pedido

    # @property
    # def total(self):
    #     return self.lineapedido_set_aggregate(
    #
    #         total=Sum( F("precio") * F("cantidad"), output_field=FloatField)
    #
    #
    #     )["total"] # set_aggregate me vas a agregar el total y autput_field es que de salida me vas a dar un valor float

    class Meta:
        db_table= "pedidoss" #el nombre que va a tener la tabla en la BBDD
        verbose_name= "pedido"
        verbose_name_plural= "pedidoss"
        ordering = ['id'] #significa que se va a ordenar por id



class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete= models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete= models.CASCADE)
    cantidad = models.IntegerField(default=1) # por defecto le damos el valor de 1
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}' # la f es de formato



    class Meta:
        db_table= "Lineapedidos" #el nombre que va a tener la tabla en la BBDD
        verbose_name= "Linea Pedido"
        verbose_name_plural= "Lineas Pedidos"
        ordering = ['id'] #significa que se va a ordenar por id





