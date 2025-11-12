from django.http import HttpResponse

def saludo(req):
    return HttpResponse("Hola Mundo")

def despedida(req):
    return HttpResponse("Adiós Mundo")

def adulto(req, edad):
    if edad >= 18:
        return HttpResponse("Eres mayor de edad")
    return HttpResponse("No eres mayor de edad")