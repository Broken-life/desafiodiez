from django.shortcuts import render, HttpResponse

# Create your views here.
def about(request): #buscar forma de linkear css en django
    return HttpResponse("<h1 style='color:red';>Grupo Pyhtoneers formado en el año 2023 durante el Informatorio</h1>")