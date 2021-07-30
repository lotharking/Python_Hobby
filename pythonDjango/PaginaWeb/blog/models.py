from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    # change the behavor in the model class
    class Meta:
        verbose_name='categoria' # is the name of the table
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre

class post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='post', null= True, blank = True) 
    autor = models.ForeignKey(User, on_delete=models.CASCADE) # ForeignKey --> indica que al usuario le pertenecen los posts
    categoria = models.ManyToManyField(categoria) # ManyToManyField --> establece relacion de varios a varios con la clase categorias
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.titulo

