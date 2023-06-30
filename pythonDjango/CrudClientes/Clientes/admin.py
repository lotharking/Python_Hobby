from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "correo", "telefono")
    search_fields = ("nombre", "apellido")