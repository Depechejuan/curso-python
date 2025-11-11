from django.http import HttpResponse

def saludo(req):
    return HttpResponse("Hola Mundo")

def despedida(req):
    return HttpResponse("Adiós Mundo")