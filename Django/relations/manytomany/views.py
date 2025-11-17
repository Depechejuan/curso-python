from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Publication

# Create your views here.
def create(req):
    art1 = Article(headline="Articulo 1")
    art2 = Article(headline="Articulo 2")
    art3 = Article(headline="Articulo 3")
    art1.save()
    art2.save()
    art3.save()

    pub1 = Publication(title="Publicacion 1")
    pub2 = Publication(title="Publicacion 2")
    pub3 = Publication(title="Publicacion 3")
    pub4 = Publication(title="Publicacion 4")
    pub5 = Publication(title="Publicacion 5")
    pub6 = Publication(title="Publicacion 6")
    pub7 = Publication(title="Publicacion 7")
    pub1.save()
    pub2.save()
    pub3.save()
    pub4.save()
    pub5.save()
    pub6.save()
    pub7.save()

    art1.publications.add(pub1)
    art1.publications.add(pub2)
    art1.publications.add(pub3)
    art2.publications.add(pub4)
    art2.publications.add(pub5)
    art3.publications.add(pub6)
    art3.publications.add(pub7)

    art3.publications.remove(pub7)

    result = art3.publications.all()

    return HttpResponse(result)