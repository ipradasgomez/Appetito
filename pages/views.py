from django.shortcuts import render
from plans.models import Plan
from cartas.models import Plato, Tag
from restaurantes.models import Restaurante
from django.db.models import Q
# Create your views here.

def about(request):
    return render(request, 'pages/about.html', {'nav_home': 'active'})

def search(request):
    #Filtrar por nombre y tag
    query = Q(nombre__contains=request.GET['q'].strip())
    query.add(Q(tags__in=Tag.objects.filter(tagtext__contains=request.GET['q'].strip())), Q.OR)

    #Filtrar por precio
    pm = request.GET.get('pm', '')
    if pm and pm.strip() is not '' and pm.strip() is not '0':
        query.add(Q(precio__lt=pm), Q.AND) 
    
    all_results = Plato.objects.filter(query)

    #Filtrar por distancia
    near_rest_ids=[]
    near_ub_ids=[]
    r = request.GET.get('r', '')
    clt = request.GET.get('current_lat', '')
    cln = request.GET.get('current_lon', '')

    if r and clt and cln and r.strip() is not '' and r.strip() is not '0' and clt.strip() is not '' and cln.strip() is not '':
        for plato in all_results:
            for direc in plato.categoria.restaurante.direcciones.filter(restaurante_id=plato.categoria.restaurante.id):
                print(direc.id)
                if direc.en_radio(r, clt, cln):
                    near_rest_ids.append(plato.categoria.restaurante.id)
                    near_ub_ids.append(direc.id)
        all_results = all_results.filter(categoria__restaurante__id__in=near_rest_ids)

    #Obtener direcciones validas
    #for plato in all_results:
    #   for direc in plato.categoria.restaurante.direccion:

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