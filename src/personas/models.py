from django.db import models

class Persona(models.Model):
    nombres   = models.TextField()
    apellidos = models.TextField()
    edad      = models.IntegerField()
# Create your models here.
