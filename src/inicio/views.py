from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(*args, **kwargs):
    print("Esta es una vistaa:", args)
    return HttpResponse('<h1>Hola mundo</h1>')
