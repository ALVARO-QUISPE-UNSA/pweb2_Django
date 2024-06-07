from django.db import models

class Persona(models.Model):
    nombres   = models.TextField()
    apellidos = models.TextField()
    edad      = models.IntegerField()
    donador   = models.BooleanField()
    direccion = models.TextField(max_length=30, null=False, blank=False)
# Create your models here.
