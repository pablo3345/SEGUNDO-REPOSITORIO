from django.db import models

# Create your models here.


class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "categoriaProducto"   # para el nombre en singulas
        verbose_name_plural = "categoriasProducto" # para el nombre en plural

    def __str__(self):
        return  self.nombre # metodo string para que nos devuelva el nombre de la categoria, para que se vean los nombres en el panel de adm.


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE) # clave foranea (capaz que sea uno a muchos)
    imagen = models.ImageField(upload_to="tienda", null=True, blank=True) #upload_to (es para decir donde vamos a dejar las imagenes cargadas, en que directorio), null= True(para decirle que las imagenes las podemos dejar en blanco), )
    precio = models.FloatField()
    disponibilidad= models.BooleanField(default=True) # para decirle si un producto esta disponible o no, con default=True le digo que por defecto este disponible el producto
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
