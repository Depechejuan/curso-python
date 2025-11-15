from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

# Create your views here.
def test(req):
    return HttpResponse("funciona correctamente")

def create(req):
    # comment = Comment(name="Juanjo", score=5, comment="Esto es un comentario")
    # comment.save()

    # comment = Comment.objects.create(name="Alex")
    return HttpResponse("TODO")

def delete(req):
    # comment = Comment.objects.get(id=1)
    # comment.delete()
    # Comment.objects.filter(id=2).delete()
    return HttpResponse("Usuario borrado")