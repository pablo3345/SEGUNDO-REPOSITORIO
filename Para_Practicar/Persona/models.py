from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad =models.IntegerField()

    class Meta:
        db_table = 'persona'
        verbose_name = 'persona'
        verbose_name_plural = 'personas'

    def __str__(self):
        return self.nombre

