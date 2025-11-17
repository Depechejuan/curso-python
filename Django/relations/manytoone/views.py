from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date
# Create your views here.
def create(req):
    reporter = Reporter(first_name="Juan", last_name="Leon", email="email@gmail.com")
    reporter.save()
    art1 = Article(headline="Lorem ipsum", pub_date=date(2025,10,11), reporter=reporter)
    art1.save()
    art2 = Article(headline="Lorem ipsum sit dolor", pub_date=date(2025,10,15), reporter=reporter)
    art2.save()
    art3 = Article(headline="Articulo 3 diferente", pub_date=date(2025,10,17), reporter=reporter)
    art3.save()

    # result = art1.reporter.first_name
    # result = reporter.article_set.all()
    # result = reporter.article_set.filter(headline="Articulo 3 diferente")
    result = reporter.article_set.count()

    return HttpResponse(result)