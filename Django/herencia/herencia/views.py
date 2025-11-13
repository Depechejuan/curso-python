from django.shortcuts import render

def index(req):
    return render(req, "index.html", {})

def herencia(req):
    return render(req, 'herencia.html', {})

def ejemplo(req):
    return render(req, 'ejemplo.html', {})

def otra(req):
    return render(req, 'otra.html', {})


def foto(req):
    return render(req, 'foto.html', {})

def portfolio(req):
    return render(req, 'portfolio.html', {})

def about(req):
    return render(req, 'about.html', {})