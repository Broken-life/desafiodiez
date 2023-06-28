from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse(f"<h1>¡Hola Lucas!</h1> <h2> <b>Este es nuestro home :D </h2> </b> <br> Integrantes del grupo <b><u>Pythoneers</u></b>: <br> -Yrala Fabian <br>-Morinigo Pedro <br>-Sosa Fogar Yamila Noel <br>-Palacios Meyer Néstor Gustavo <br>-Cuquejo Daira <br>-Bazan Julio Pablo Federico <br>-Gonzalez Juan Ignacio")

def about(request):
    return HttpResponse("<h1 style='color:red';>Grupo Pyhtoneers formado en el año 2023 durante el inforamtorio</h1>")
