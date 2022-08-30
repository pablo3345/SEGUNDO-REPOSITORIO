

def importe_total_carro(request):
    total=0 #esta es la variable global
    if request.user.is_authenticated: # para saber si el usuario esta autenticado, debo logearme para que me aparezca el total
      for key, value in request.session["carro"].items(): # para cada clave valor de los elementos del carro
         total=  total+float(value["precio"])

    '''else:
        total="Debes hacer login"'''
    return {"importe_total_carro": total} # a la variable importe_total_carro le agrego el total

