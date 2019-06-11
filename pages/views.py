from django.shortcuts import render
from plans.models import Plan
from cartas.models import Plato, Tag
from restaurantes.models import Restaurante
from django.db.models import Q
# Create your views here.

def about(request):
    return render(request, 'pages/about.html', {'nav_home': 'active'})

def search(request):
    query = Q(nombre__contains=request.GET['q'].strip())
    query.add(Q(tags__in=Tag.objects.filter(tagtext__contains=request.GET['q'].strip())), Q.OR)
    #query.add(Q(last_name='doe'), Q.AND)
    pm = request.GET.get('pm', '')
    if pm and pm.strip() is not '' and pm.strip() is not '0':
        query.add(Q(precio__lt=pm), Q.AND)

    r = request.GET.get('r', '')
    if r and r.strip() is not '' and r.strip() is not '0':
        query.add(Q(categoria__restaurante__direcciones__lat__lt=1), Q.AND)   
    
    all_results = Plato.objects.filter(query)

    context={
        'results': all_results
    }
    return render(request, 'pages/search.html', context)

def landing(request):
    return render(request, 'pages/landing.html', {'nav_home': 'active', 'plans': Plan.objects.all()})

def restaurante(request, id):
    if Restaurante.objects.filter(pk=id).exists():        
        context = {
            'exist': True,
            'restaurante': Restaurante.objects.get(pk=id)
        }
        pass
    else:
        context = {
            'exist': False
        }
    return render(request, 'pages/restaurante.html', context)