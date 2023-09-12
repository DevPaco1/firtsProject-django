from django.shortcuts import render

#importer HTTPResponse
from django.http import HttpResponse
from django.template import loader

#Las vistas son funciones
def bienvenida(request):
    #Response
    return HttpResponse("Bienvenido")

def despedida(request):
    return HttpResponse("Despedida")

def saludo(request):
    return HttpResponse("Saludando a koders")

def saludar_con_nombre(request, nombre):
    context = {
        "name": nombre,
        "apellido": "paez"
        }
    template = loader.get_template("base.html")
    return HttpResponse(template.render(context, request))

def mentor(request, user):
    return HttpResponse("Hello mentor here are youy classes")

def mentor_koder(request, user):
    if user == "koder": 
        resultado = ("Hello koder welcome to kodemia")
    elif user == "mentor":
        resultado = ("Hello mentor here are youy classes")
    else:
        resultado = ("you are not welcome here")

    return HttpResponse(resultado)

def type_and_name(request, name, type):
    context = {"name": name,"type": type}
    template =loader.get_template("type_and_name.html")
    return HttpResponse(template.render(context,request))