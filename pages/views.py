from django.shortcuts import render
from plans.models import Plan
from cartas.models import Plato, Tag
from restaurantes.models import Restaurante
from django.db.models import Q

##PDF
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape
from django.conf import settings
import os
##OtroPDF
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
    near_rest_ids = []
    near_ubs = []
    r = request.GET.get('r', '')
    clt = request.GET.get('current_lat', '')
    cln = request.GET.get('current_lon', '')

    if r and clt and cln and r.strip() is not '' and r.strip() is not '0' and clt.strip() is not '' and cln.strip() is not '':
        for plato in all_results:
            for direc in plato.categoria.restaurante.direcciones.filter(restaurante_id=plato.categoria.restaurante.id):
                if direc.en_radio(r, clt, cln):
                    near_rest_ids.append(plato.categoria.restaurante.id)
                    near_ubs.append(direc)
        all_results = all_results.filter(categoria__restaurante__id__in=near_rest_ids)
    else:
        for plato in all_results:
            for direc in plato.categoria.restaurante.direcciones.filter(restaurante_id=plato.categoria.restaurante.id):
                near_rest_ids.append(plato.categoria.restaurante.id)
                near_ubs.append(direc)
        all_results = all_results.filter(categoria__restaurante__id__in=near_rest_ids)
    
    context={
        'results': all_results,
        'direcs':near_ubs
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

def respdf(request, id):
    exist = Restaurante.objects.filter(pk=id).exists()
    if(exist):
        rest = Restaurante.objects.get(pk=id)
    else:
        rest = None
    return render_to_pdf(
            'pages/restaurante_pdf.html',
            {
                'pagesize':'A4',
                'restaurante': rest,
                'exist': exist
            }
        )

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = context_dict
    html = template.render(context)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), dest=result, link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def fetch_resources(uri, rel):
    path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))

    return path