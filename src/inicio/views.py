from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(*args, **kwargs):
    print("Esta es una vista:", args[0])
    print("Debería de capturar el int", kwargs)
    return HttpResponse('<h1>Hola mundo</h1>')
