from django import forms

class FormularioContacto(forms.Form): # hereda de forms Form
    nombre = forms.CharField(label="Nombre", required=True)
    email = forms.CharField(label="Email", required=True) # con true requerido le digo si el contenido es requerido o no, osea que si o si que que llenar los casilleros
    contenido = forms.CharField(label="Contenido", widget=forms.Textarea)

