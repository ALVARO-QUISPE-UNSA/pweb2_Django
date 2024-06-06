from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request, *args, **kwargs):
    dic_get = request.GET
    print (dic_get)
    print("args: ", args)
    print("kwargs: ", kwargs)
    print(request.user)
    return render(request, "home.html", {})

def anotherView (request):
    return HttpResponse('<h1>Solo otra página</h1>')
