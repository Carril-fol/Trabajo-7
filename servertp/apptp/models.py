from django.db import models

# Create your models here.
class Empresa(models.Model):

    empresa = models.CharField(max_length=250)
    dedicacion = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.empresa} / {self.dedicacion}'

class Empleado(models.Model):

    nombre_completo = models.CharField(max_length=50)
    puesto = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.nombre_completo} / {self.puesto}'

class Producto(models.Model):

    nombre_producto = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.nombre_producto}'
