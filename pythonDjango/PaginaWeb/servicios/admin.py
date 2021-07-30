from django.contrib import admin
from .models import Servicio

# Register your models here.

# Añadir campos de created y updated para mostrar
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

# Resgistrando el modelo en la parte de admin
admin.site.register(Servicio, ServicioAdmin)