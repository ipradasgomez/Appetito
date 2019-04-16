from django.shortcuts import render
from plans.models import Plan
# Create your views here.

def about(request):
    return render(request, 'pages/about.html', {'nav_home': 'active'})

def search(request):
    return render(request, 'pages/search.html', {'nav_search': 'active'})

def landing(request):
    return render(request, 'pages/landing.html', {'nav_home': 'active', 'plans': Plan.objects.all()})