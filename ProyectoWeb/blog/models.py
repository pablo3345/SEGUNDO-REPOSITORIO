from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)  # aca guardamos la fecha que se creo un servicio
    updated = models.DateTimeField(auto_now_add=True)  # si este servicio se ha modificado, guardamos la fecha que se modifico, corregirlo xq esta mas escrito

    class Meta:
        verbose_name = 'categoria'  # esto sirve para especificar el nombre que quiero que tenga el modelo dentro de la base de datos
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)  # con esto dentro de la carpeta media me va a crear una subcarpeta 'servicios' donde va a incluir las imagenes
    autor = models.ForeignKey(User, on_delete=models.CASCADE) # seria relacion uno a muchos, un autor o usuario puede tener varios post
    categorias= models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=True)     # null=True, blanck = True (con esto le digo que es opcional si quiero ingresar o guardar una imagen)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'post'  # esto sirve para especificar el nombre que quiero que tenga el modelo dentro de la base de datos
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.titulo