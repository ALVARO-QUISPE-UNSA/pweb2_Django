"""
URL configuration for listaContactos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import render
from django.urls import path

from inicio.views import anotherView, myHomeView
from personas.models import Persona
from personas.views import personaTestView, personaCreateView, personasAnotherCreateView, searchForHelp

def personasShowObjects(request, myID):
    obj = Persona.objects.get(id=myID)
    context = {
        'objeto': obj,
    }
    return render(request, 'personas/descripcion.html', context)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myHomeView, name='Página de inicio'),
    path('another/', anotherView, name='otro'),
    path('persona/', personaTestView, name='otro'),
    path('add/', personaCreateView, name='createPersona'),
    path('anotherAdd/', personasAnotherCreateView, name='OtroAgergarPersonas'),
    path('search/', searchForHelp, name='buscar'),
    path('personas/<int:myID>/', personasShowObjects, name = 'browsing')
]

