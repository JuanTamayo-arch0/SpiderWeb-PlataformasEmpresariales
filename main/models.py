from django.db import models

# Create your models here.

class SpidermanVariant(models.Model):
    imagen = models.TextField()
    nombre = models.TextField()
    datos = models.TextField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre