from django.shortcuts import render
from plans.models import Plan
from cartas.models import Plato
# Create your views here.

def about(request):
    return render(request, 'pages/about.html', {'nav_home': 'active'})

def search(request):
    results = Plato.objects.filter(nombre__contains=request.GET['q'])
    context={
        'results': results
    }
    return render(request, 'pages/search.html', context)

def landing(request):
    return render(request, 'pages/landing.html', {'nav_home': 'active', 'plans': Plan.objects.all()})