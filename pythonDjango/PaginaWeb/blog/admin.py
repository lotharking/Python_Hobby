from django.contrib import admin
from .models import categoria, post

# Register your models here.

# Añadir campos de created y updated para mostrar
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

# Resgistrando el modelo en la parte de admin
admin.site.register(categoria, CategoriaAdmin)
admin.site.register(post, PostAdmin)
