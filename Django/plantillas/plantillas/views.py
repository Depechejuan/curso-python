from django.shortcuts import render

def simple(req):
    return render(req, 'simple.html', {}) 


def dinamico(req, name):
    categories = ["code", "design", "marketing", "businesss"]
    context = { 'name': name, 'categories' : categories}
    return render(req, 'dinamico.html', context) 