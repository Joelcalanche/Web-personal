from django.shortcuts import render
from .models import Project

# Create your views here.

    
def portfolio(request):
    # esto nos devolvera todos los objetos dque tiene la clase proyecto
    projects = Project.objects.all()
    # agregamos el diccionario de contexto
    return  render(request,"portfolio/portfolio.html", {'projects': projects })