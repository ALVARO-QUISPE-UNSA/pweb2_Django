from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm

contador = 0
def personaTestView(request):
    obj = Persona.objects.get(id=1)
    context = {
        'objeto': obj,
    }
    return render(request, 'personas/descripcion.html', context)

def personaCreateView(request):
    context = {
        'llenado': False,
        'contador': contador,
    }
    if request.method == 'POST':
        contador += 1
        nombre = request.POST.get('q')
        print(nombre)
        context['llenado'] = True
    return render(request, 'personas/personasCreate.html', context)

def searchForHelp(request):
    return render(request, 'personas/search.html', {})
