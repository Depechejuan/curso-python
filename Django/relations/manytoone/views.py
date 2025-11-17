from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article

# Create your views here.
def create(req):
    reporter = Reporter("Juan", "Leon", "email@gmail.com")

    return HttpResponse("Creado")