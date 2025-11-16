from django.shortcuts import render

def foto(req):
    return render(req, 'index.html', {})

def portfolio(req):
    return render(req, 'portfolio.html', {})

def about(req):
    return render(req, 'about.html', {})