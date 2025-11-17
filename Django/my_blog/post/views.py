from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Entry

def update(req):
    author = Author.objects.get(id=1)
    author.name = "Juan"
    author.email = "email@mail.com"
    author.save()

    return HttpResponse("Update")


# Create your views here.
def queries(req):
    #Obtener todos los elementos.
    authors = Author.objects.all()

    #filtrado por condicion (Podrían ser varios, hay que iterar)
    filtered = Author.objects.filter(email='michael39@example.com')

    author = Author.objects.get(id=1)

    limit = Author.objects.all()[:10]

    #
    orders = Author.objects.all().order_by('email')

    return render(req, 'post/queries.html', { 'authors': authors, 'filtered': filtered, 'author': author, 'limit': limit, 'orders': orders})