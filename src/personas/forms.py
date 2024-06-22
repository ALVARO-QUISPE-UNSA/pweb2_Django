from django import forms
from django.forms import fields
from .models import Persona

class PersonaForm (forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombres',
            'apellidos',
            'edad',
        ]

class RawPersonaForm(forms.Form):
    nombres = forms.CharField()
    apellidos = forms.CharField()
    edad = forms.IntegerField()
    donador = forms.BooleanField()
