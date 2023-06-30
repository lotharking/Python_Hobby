from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre