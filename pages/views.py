from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def about(request):
    return render(request, 'pages/about.html')

def search(request):
    return render(request, 'pages/search.html')

def landing(request):
    return render(request, 'pages/landing.html')