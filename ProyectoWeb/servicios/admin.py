from django.contrib import admin
from .models import servicio # .modeles = el punto es porque esta en el mismo directorio que admin

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') # es de solo lectura porque no vamos a ingresar valores, se ingresa automaticamente

admin.site.register(servicio, ServicioAdmin)
