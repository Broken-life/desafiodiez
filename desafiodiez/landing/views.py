from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Hola Lucas :)</h1> <h2>Bienvenido a la mejor página de la historia 😎</h2> Mas información en /home")