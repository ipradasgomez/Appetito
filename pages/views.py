from django.shortcuts import render
from plans.models import Plan
from cartas.models import Plato, Tag
from restaurantes.models import Restaurante
# Create your views here.

def about(request):
    return render(request, 'pages/about.html', {'nav_home': 'active'})

def search(request):
    results_by_name = Plato.objects.filter(nombre__contains=request.GET['q'].strip())
    results_with_tags = Plato.objects.filter(tags__in=Tag.objects.filter(tagtext__contains=request.GET['q'].strip()))
    context={
        'results': results_by_name.union(results_with_tags)
    }
    return render(request, 'pages/search.html', context)

def landing(request):
    return render(request, 'pages/landing.html', {'nav_home': 'active', 'plans': Plan.objects.all()})

def restaurante(request, id):
    if Restaurante.objects.filter(pk=id).exists():        
        context = {
            'exist': "ok",
            'restaurante': Restaurante.objects.get(pk=id)
        }
        pass
    else:
        context = {
            'exist': "nok"
        }
    return render(request, 'pages/restaurante.html', context)