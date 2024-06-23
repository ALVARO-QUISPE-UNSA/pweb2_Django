from django import forms
from django.forms import Widget, fields
from .models import Persona

class PersonaForm (forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombres',
            'apellidos',
            'edad',
            'donador',
        ]
    def clean_nombres(self, *args, **kwargs):
        print('pasó')
        name = self.cleaned_data.get('nombres')
        if name.istitle():
            return name
        else :
            raise forms.ValidationError('Oe, la primera letra en mayúscula Ignorante')

class RawPersonaForm(forms.Form):
    nombres = forms.CharField(
        widget = forms.Textarea(
            attrs={
                'placeholder': 'Sólo tu nombre por favor',
                'id': 'nombreID',
                'class': 'special',
                'cols': '10',
            }
        )
    )
    apellidos = forms.CharField()
    edad = forms.IntegerField(initial=20)
    donador = forms.BooleanField()
