from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('''<h1>¡Hola Lucas!</h1> 
    <h2><b>Este es nuestro home :D </b></h2>
    <p>Integrantes del grupo <b><u>Pythoneers</u>:</b></p> 
    <ul>
        <li>Yrala Fabian</li>
        <li>Morinigo Pedro</li>
        <li>Sosa Fogar Yamila Noel</li>
        <li>Palacios Meyer Néstor Gustavo</li>
        <li>Cuquejo Daira</li>
        <li>Bazan Julio Pablo Federico</li>
        <li>Gonzalez Juan Ignacio</li>
    </ul>''')

def about(request): #buscar forma de linkear css en django
    return HttpResponse("<h1 style='color:red';>Grupo Pyhtoneers formado en el año 2023 durante el Informatorio</h1>")
