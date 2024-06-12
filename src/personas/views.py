from django.shortcuts import render
from .models import Persona

def personaView(request):
    obj = Persona.objects.get(id=1)
    context = {
        'nombre': obj.nombres,
        'edad': obj.edad,
    }
    return render(request, 'personas/tests.html', context)
