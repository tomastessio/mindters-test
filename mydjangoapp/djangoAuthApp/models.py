from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=150, unique=True)
    correo_electronico = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre_usuario

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre