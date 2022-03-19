class Carro: # es una clase
    def __init__(self, request): #el constructor vamos a recibir por parametro el self y la peticion(request)
        '''self.request = request # aca ya tenemos en la variable de tipo request almacenada la peticion
        self.session = request.session #con esto tenemos iniciada la sesion, por si me voy del carro y vuelvo despues (cuando le doy atras al google)
        carro = self.session.get("carro")  #ahora debemos construir un carro de la compra para esta sesion, que el usuario habra iniciada
        if not carro:             #esto es si no hay carro, me lo creas
            carro= self.session["carro"]= {} #un diccionario vacio
       # else:'''
        self.carro = carro # si el usuario estaba rellenando el carro y se fue de la pagina por cualquier motivo y despues vuelve, (bueno es el carro de la sesion que ya habia y esta fuera del if)

    def agregarProducto(self, producto):
        if(str(producto.id) not in self.carro.keys()): #funcion string para pasar el id del producto a string, con el metodo keys veo las clave almacenadas en el carro, esto significa que si el producto no esta en el carro lo agrega(xq no puedo agregar un producto que ya esta en el carro), si el id del producto no esta en las claves de nuestro carro
            self.carro[producto.id] = {"producto_id": producto.id, # esto es clave valor (self.carro[producto.id] es la clave y el valor es el diccionario)
                                       "nombre": producto.nombre,
                                       "precio": str(producto.precio), # estaba numerico lo pasamos a string
                                       "cantidad": 1, #al principio se agrega un producto, despues se agregan mas, se agraga de uno en uno
                                        "imagen": producto.imagen.url #para ir a la url donde estan las imagenes
                                       }


        else: # por si ya esta el producto en el carro, recorremos con un for
            for key, value in self.carro.items(): # key value significa para cada clave valor
                if key == str(producto.id): #comprobar si la clave se corresponde con algunos productos que ya tenemos en el carro
                    value["cantidad"] = value["cantidad"]+1 # si esta ese producto al valor cantidad me lo incrementas en uno
                    value["precio"] = float(value["precio"])+ producto.precio # para que me incremente el precio en el carro cuando agrego
                    break # si ya lo encontro ya no recorras mas los elementos

       # ahora lo que debemos hacer es actualizar ese carro para almacenarlo en la sesion, cada paso que hacemos deberia guardarlo en la sesion (no lo hacemos en el if else)

        self.guardar_carro() # llamo a esta funcion para actualizar la sesion cada vez que hagmos una operacion de agregar, restar etc etc


    def guardar_carro(self): #metodo para actualizar la sesion tanto cuando agrego o resto etc
        self.session["carro"] = self.carro # el carro debe ser igual al carro de la sesion que estamos manejando ahora mismo, y para que tome efecto usamos "modifed"
        self.session.modifed = True # se modifico la sesion despues de agregar, restar etc? si..entonces True



    def eliminar(self, producto): #recibe por parametro el producto que queremos eliminar, aclaramos que eliminar no es lo mismo que restar, podemos eliminar un producto con 100 unidades y podemos restar una unidad de un producto
         producto.id = str(producto.id) # lo primero que hacemos el id del producto debe ser igual al id pasado por string
         if producto.id in self.carro: # si esto esta en el carro me lo quitas
             del self.carro[producto.id] # el metodo del es para eliminar del carro
             self.guardar_carro() # para actualizar el carro con la sesion



    def restar_producto(self, producto): # recibe por parametro el producto del cual queremos restar unidades
        for key, value in self.carro.items(): # para cada clave valor que encuentres en los elementos del carro
            if key == str(producto.id): # si la clave corresponde al id del producto
               value["cantidad"] = value["cantidad"] -1 # me restas uno, parte de este codigo lo copie del else de arriba
               value["precio"] = float(value["precio"]) - producto.precio # para que reste en el carro cuando resto unidades
               if value["cantidad"] <1: # este if es por si queda un solo producto y quiere restarle uno, entonces que me lo elimine
                   self.eliminar(producto)
               break

        self.guardar_carro() # me actualiza el carro



    def limpiar_carro(self): # por si agregue 20 productos y me arrepiento y quiero limpiar el carro
        self.session["carro"] = {} # un carro vacio, en la sesion en la que estoy
        self.session.modifed = True # la sesion fue modificada entonces True.




# la clave es el id del producto mientras que el valor es el diccionario ej: precio, nombre, imagen etc
# ver en video 52 de django pildorasInformaticas