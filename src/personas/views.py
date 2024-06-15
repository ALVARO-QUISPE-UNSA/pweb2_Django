from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm

contador = 0
comentarios = []
def personaTestView(request):
    obj = Persona.objects.get(id=1)
    context = {
        'objeto': obj,
    }
    return render(request, 'personas/descripcion.html', context)

def personaCreateView(request):
    global contador
    global comentarios
    context = {
        'llenado': False,
        'contador': contador,
        'comentarios': comentarios,
    }
    if request.method == 'POST':
        contador += 1
        nombre = request.POST.get('q')
        com = request.POST.get('comentario')
        comentarios.append(com)
        print(nombre)
        context['llenado'] = True
    return render(request, 'personas/personasCreate.html', context)

def searchForHelp(request):
    return render(request, 'personas/search.html', {})
