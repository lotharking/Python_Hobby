from django.db.models.fields.files import ImageField
from blog.models import categoria
from django.db import models

# Create your models here.

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    # change the behavor in the model class
    class Meta:
        verbose_name='categoriaProd' # is the name of the table
        verbose_name_plural='categoriasProd'

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='tienda', null= True, blank = True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    cantidad = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'

    def __str__(self):
        return self.nombre
