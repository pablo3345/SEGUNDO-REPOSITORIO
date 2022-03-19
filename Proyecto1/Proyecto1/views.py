from django.http import HttpResponse
from django.template import Template, Context
import datetime
from django.template.loader import get_template #esto me sirve para cargar las plantillas o template
from django.shortcuts import render #con esto saco en el ruturn httpResponse y pongo el render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre= nombre
        self.apellido=apellido

def saludo(request):
    p1=Persona("Claudio", "Peruchi") #creo un objeto de la clase persona de arriba
    listaVavia = [] #si la lista es vacia en el html del if pasa al else, sino muestra el contenido
    nombre = "Pablo"  # para pasarsela a la plantilla, debemos pasrla al contexto con un diccionario
    apellido ="Peruchi"# tambien se le puede poner el valor directamente en el diccionario del contexto
    ahora = datetime.datetime.now() #tambien la paso en el diccionario del contexto
    nombresLista = ["pablo", "Lucas", "Martin", "Steve", "Diego"] #creo una variable para pasarle una lista en el contexto y verla en las plantillas
    ############################################################################################################
    #documento_externo le marco la ruta de la plantilla, luego uso el objejo Template para pasarle el documento_externo y con read la lee
    #luego le decimos que renderice el objeto Template y le pasamos un contexto
   # documento_externo = open("C:/Users/pablo/Desktop/ProyectoDjango/Proyecto1/Proyecto1/plantillas/index.html")
   # plantilla = Template(documento_externo.read())
   # documento_externo.close()

   # documentoExterno = get_template('index.html') #si quiero cargar 5 o 6 plantillas mas solo tengo que poner esto
   # contexto = Context({"nombre_persona": nombre ,"apellido_persona": apellido, "fecha": ahora,
    #                    "nombreObjeto": p1.nombre, "apellidoObjeto": p1.apellido, "temasDelCurso":["Plantillas", "Modelos", "formularios", "Vistas"],
     #                   "listaNombre":nombresLista, "listaVacia": listaVavia})
   # documento = (documentoExterno.render({"nombre_persona": nombre ,"apellido_persona": apellido, "fecha": ahora,
           #            "nombreObjeto": p1.nombre, "apellidoObjeto": p1.apellido, "temasDelCurso":["Plantillas", "Modelos", "formularios", "Vistas"],
             #          "listaNombre":nombresLista, "listaVacia": listaVavia}))#los template de antes y ahora no son iguales, antes el render recibia un contexto y ahora recibe un diccionario directamente
                                                                     #esta forma simple sirve mas para proyectos donde cargo muchas plantillas, cualquier cosa fijarme en el video 8 (para una sola plantilla)




    return render(request, "index.html", {"nombre_persona": nombre ,"apellido_persona": apellido, "fecha": ahora,
                       "nombreObjeto": p1.nombre, "apellidoObjeto": p1.apellido, "temasDelCurso":["Plantillas", "Modelos", "formularios", "Vistas"],
                       "listaNombre":nombresLista, "listaVacia": listaVavia})
    #recibe el request, el archivo html y opcional el diccionario



def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """<html><body><h1>Fecha y hora actual %s</h1><body/></html//>"""%fecha_actual
    # %s marcador de posicion

    return HttpResponse(documento)

def calculaEdad(request, agnio):
    edadActual = 42
    periodo = agnio -2021
    edadFutura = edadActual+periodo
    documento = "<html><body><h2>En el año %s tendras %s años</h2>" %(agnio, edadFutura)

    #pasar datos por parametro
    return HttpResponse(documento)


def crearUnLink(request):
    return render(request, "index2.html")


def cursosDeInformatica(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "cursoDeInformatica.html", {"dameFecha": fecha_actual})


def cursosDeInformatica2(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "cursoDeInformatica2.html", {"dameFecha": fecha_actual})
