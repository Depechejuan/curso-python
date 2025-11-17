from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant

# Create your views here.
def create(req):
    place = Place(name="Lugar 1", address="Carlle Demo")
    place.save()
    restaurant = Restaurant(place=place, num_of_employees=8)
    restaurant.save()


    return HttpResponse(restaurant.place)