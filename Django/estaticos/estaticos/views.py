from django.shortcuts import render

def estaticos(req):
    return render(req, 'estaticos.html', {})