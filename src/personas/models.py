from django.db import models
from django.urls import reverse

class Persona(models.Model):
    nombres   = models.TextField()
    apellidos = models.TextField()
    edad      = models.IntegerField()
    donador   = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('browsing', kwargs={'myID': self.id})
