from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre= models.CharField(max_length=30) #declaro la variable, el tipo de dato y la longitud de esa dato o variable
    direccion = models.CharField(max_length=50, verbose_name="La direccion")
    email = models.EmailField(blank = True, null= True) #con estos valores que le puse me permite dejar el casillero en blanco en
                                                        # el panel y que no sea obligatorio rellenarlos
    telefono = models.CharField(max_length=7)

    def __str__(self):
        return self.nombre #esto es solo para que en el panel me aparezca el nombre y no el objeto

class Articulos(models.Model):
    nombre= models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return 'el nombre es %s la seccion es %s y el precio es %s' %(self.nombre, self.seccion, self.precio)
    #el metodo string para que cuando hago la consulta con la base de datos me traiga todos los datos y no solo el id
    # asi tambien me lo muestra en el panel de administracion


class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField() # para saber si un pedido fue entregado entonces sera True


