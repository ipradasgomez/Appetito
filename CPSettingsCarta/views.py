from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cartas.models import Categoria, Plato, Tag
from django.contrib import messages
from cartas.forms import PlatoCreateForm

@login_required(login_url='/account/login')
def menu_cat_view(request):
    context = {
        'foodForm' : PlatoCreateForm()
    }
    return render(request, 'CPSettingsCarta/index.html', context)

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
    if request.POST:
        if request.user.profile.restaurante.categorias.filter(pk=request.POST['categoria_id']).exists():
            categoria = request.user.profile.restaurante.categorias.get(pk=request.POST['categoria_id'])
            if categoria.platos.count() < request.user.profile.plan.max_productos_x_cat or request.user.profile.plan.max_productos_x_cat is 0:
                form = PlatoCreateForm(request.POST, request.FILES)
                if form.is_valid():
                    plato = form.save(commit=False)
                    categoria.platos.add(plato, bulk=False)
                    categoria.save()
                else:
                    messages.error(request, "Se han encontrado errores: "+' '.join(form.errors))
            else:
                messages.error(request, 'Esta categoría no acepta más productos... ¡Incrementa tu plan!')
        else:
            messages.error(request, 'No puedes añadir un plato a esta categoría.')
    return redirect('settings_menu_view')

@login_required(login_url='/account/login')
def menu_food_remove(request):
    if request.POST['foodid'] and request.POST['foodid'].strip() != '' and Plato.objects.filter(pk=request.POST['foodid']).exists():
        Plato.objects.filter(pk=request.POST['foodid']).delete()
        messages.success(request, 'Plato eliminado.')
    else:
        messages.error(request, "Imposible eliminar el plato.")
    return redirect('settings_menu_view')

@login_required(login_url='/account/login')
def menu_food_edit(request, foodId):
    if Plato.objects.filter(pk=foodId).exists() and Plato.objects.get(pk=foodId).categoria.restaurante.id is request.user.profile.restaurante.id:
        if request.POST:
            form = PlatoCreateForm(request.POST or None, request.FILES or None, instance=Plato.objects.get(pk=foodId))
            if form.is_valid():
                form.save()
                messages.success(request, "Plato editado con éxito")
                return redirect('settings_menu_view')
        context={
            'foodId':foodId,
            'plato':Plato.objects.get(pk=foodId),
            'editForm':PlatoCreateForm(instance=Plato.objects.get(pk=foodId))
            }
        return render(request, 'CPSettingsCarta/editfood.html', context)
    else:
        messages.error(request, "Error obteniendo el plato.")
        return redirect('settings_menu_view')      

@login_required(login_url='/account/login')
def food_tag_add(request):
    if request.POST:
        if Plato.objects.filter(pk=request.POST['foodId']).exists() and Plato.objects.get(pk=request.POST['foodId']).categoria.restaurante.id is request.user.profile.restaurante.id:
            if Plato.objects.get(pk=request.POST['foodId']).tags.count() < request.user.profile.plan.max_tags_x_prod or request.user.profile.plan.max_tags_x_prod is 0:
                if request.POST['tag'].strip() is not '':
                    Tag.objects.get_or_create(tagtext=request.POST['tag'].strip())
                    tag =Tag.objects.get(tagtext=request.POST['tag'].strip())
                    plato = Plato.objects.get(pk=request.POST['foodId'])
                    plato.tags.add(tag)
                    plato.save()
                else:
                    messages.error(request, "El tag no puede estar vacio.")
            else:
                messages.error(request, "El no puedes añadir mas tags al plato. ¡Incrementa tu plan!")
        else:
            messages.error(request, "No se han encontrado el plato.")

    return redirect('settings_menu_editfood', request.POST['foodId'])

@login_required(login_url='/account/login')
def food_tag_remove(request, food, tag):
    plato = Plato.objects.get(pk=food)
    tag = Tag.objects.get(pk=tag)
    plato.tags.remove(tag)
    plato.save()
    return redirect('settings_menu_editfood', food)
