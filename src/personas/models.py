from django.db import models

class Persona(models.Model):
    nombres   = models.TextField()
    apellidos = models.TextField()
    edad      = models.IntegerField()
    donador   = models.BooleanField(default=True)

    def get_absolute_url(self):
        return "/personas/" + str(self.id) + "/"
