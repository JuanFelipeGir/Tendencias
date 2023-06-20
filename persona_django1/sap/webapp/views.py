from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def pagina_inicio(request):
    return HttpResponse("pagina_inicio")

def bienvenido(request):
    return HttpResponse("Hola mundo desde django")
def despedida(request):
    return HttpResponse("Despedida desde django")

def bienvenidohtml(request):
    return render(request, 'EstudiantesTdeA.html')

def inicio(request):
    return render(request, "inicio.html")
def contacto(request):
    return render(request, "contacto.html")




