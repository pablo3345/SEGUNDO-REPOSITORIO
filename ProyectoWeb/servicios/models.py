from django.db import models

# Create your models here.

class servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='servicios')# con esto dentro de la carpeta media me va a crear una subcarpeta 'servicios' donde va a incluir las imagenes
    created = models.DateTimeField(auto_now_add=True) #aca guardamos la fecha que se creo un servicio
    updated = models.DateTimeField(auto_now_add=True) # si este servicio se ha modificado, guardamos la fecha que se modifico

    class Meta:
        verbose_name = 'servicio' #esto sirve para especificar el nombre que quiero que tenga el modelo dentro de la base de datos
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.titulo