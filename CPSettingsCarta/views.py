from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cartas.models import Categoria, Plato
from django.contrib import messages
@login_required(login_url='/account/login')
def menu_settings_view(request):
    return render(request, 'CPSettingsCarta/index.html')

@login_required(login_url='/account/login')
def menu_cat_create(request):
    if request.POST['catname'] and request.POST['catname'].strip() != '':
        cat = request.user.profile.restaurante.categorias.create(nombre=request.POST['catname'])
        cat.save()
        messages.success(request, 'Categoría creada.')
    else:
        messages.error(request, "Introduce un nombre de categoría válido")
    return redirect('settings_menu_view')

@login_required(login_url='/account/login')
def menu_cat_remove(request):
    if request.POST['deletecatid'] and request.POST['deletecatid'].strip() != '' and request.user.profile.restaurante.categorias.filter(pk=request.POST['deletecatid']).exists():
        Categoria.objects.filter(pk=request.POST['deletecatid']).delete()
        messages.success(request, 'Categoría eliminada.')
    else:
        messages.error(request, "Imposible eliminar la categoría.")
    return redirect('settings_menu_view')

@login_required(login_url='/account/login')
def menu_cat_edit(request):
    if request.POST['catidedit'] and request.user.profile.restaurante.categorias.filter(pk=request.POST['catidedit']).exists():
        if request.POST['newcatname'] and request.POST['newcatname'].strip() != '':
            cat = Categoria.objects.filter(pk=request.POST['catidedit'])[:1].get()
            cat.nombre = request.POST['newcatname']
            cat.save()
            messages.success(request, 'Categoría editada con éxito.')
        else:
            messages.error(request, "Imposible editar la categoría.")
    else:
        messages.error(request, "Imposible editar la categoría.")
    return redirect('settings_menu_view')

@login_required(login_url='/account/login')
def menu_food_create(request):
    pass

@login_required(login_url='/account/login')
def menu_food_remove(request):
    if request.POST['deletefoodid'] and request.POST['deletefoodid'].strip() != '' and Plato.filter(pk=request.POST['deletecatid']).exists():
        Plato.objects.filter(pk=request.POST['deletefoodid']).delete()
        messages.success(request, 'Plato eliminado.')
    else:
        messages.error(request, "Imposible eliminar el plato.")
    return redirect('settings_menu_view')