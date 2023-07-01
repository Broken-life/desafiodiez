from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# crear tus vistas aquí
def home(request):
    return HttpResponse('''<h1 style='color:red'>¡Hola Lucas!</h1> 
    <h2><b>Este es nuestro home :D </b></h2>
    <p>Integrantes del grupo <b><u>Pythoneers</u>:</b></p> 
    <ul>
        <li style="color:blue";>Yrala Fabian</li>
        <li style="color:blue";>Morinigo Pedro</li>
        <li style="color:blue";>Sosa Fogar Yamila Noel</li>
        <li style="color:blue";>Palacios Meyer Néstor Gustavo</li>
        <li style="color:blue";>Cuquejo Daira</li>
        <li style="color:blue";>Bazan Julio Pablo Federico</li>
        <li style="color:blue";>Gonzalez Juan Ignacio</li>
        <a style="background:grey" href ='/'>Volver a la página principal</a>
    </ul>''')


