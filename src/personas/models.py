from django.db import models

class Persona(models.Model):
    nombres   = models.TextField()
    apellidos = models.TextField()
    edad      = models.IntegerField()
    donador   = models.BooleanField()
# Create your models here.
