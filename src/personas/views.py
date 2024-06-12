from django.shortcuts import render
from .models import Persona

def personaTestView(request):
    obj = Persona.objects.get(id=1)
    context = {
        'objeto': obj,
    }
    return render(request, 'personas/test.html', context)
