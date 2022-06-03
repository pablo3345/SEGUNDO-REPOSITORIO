from django.db import models
from tienda.models import Producto
from django.db.models import F, Sum, FloatField

# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model() # con esto mas la importacion que hice arriba me va a traer el usuario que esta logeado


class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at= models.DateTimeField(auto_now_add=True) # con auto...me registra en el instante que fue grabado

    def __str__(self):
        return self.id #para que me devuelva el id del pedido


    @property # es una propiedad
    def total(self):
        return self.lineapedido_set.aggregate( #aggregate es lo que tiene que agregar ej: una variable que se va a llamar total

        total =Sum(F("precio")* F("cantidad"), output_field=FloatField()) #F y Sum es para hacer calculos para sumar, output es la salida que es decimal, float

        )["total"] # se cierra el parentesis de aggregate y tienes que ponerme el total
    class Meta:
        db_table= 'pedidos' # el nombre de la tabla va a ser pedidos
        verbose_name ='pedido'
        verbose_name_plural = 'pedidos'
        ordering=['id'] #significa que esto se va a ordenar por id



class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)#por defecto le damos un valor de uno, para un producto x unidad
    create_at = models.DateTimeField(auto_now_add=True)  # con auto...me registra en el instante que fue grabado

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto_id.nombre}' # la f es de darle formato


    class Meta:
        db_table= 'lineapedidos' # el nombre de la tabla
        verbose_name ='Linea Pedido'
        verbose_name_plural = 'Lineas Pedidos'
        ordering=['id'] #significa que esto se va a ordenar por id







