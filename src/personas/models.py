from asyncio import shield
from django.db import models

class Persona(models.Model):
    nombres   = models.TextField()
    apellidos = models.TextField()
    edad      = models.IntegerField()
    dni       = models.IntegerField()
    def __str__(self):
        return str( self.nombres ) + " " + str( self.apellidos )
# Create your models here.
