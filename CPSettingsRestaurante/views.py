from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from restaurantes.models import Restaurante, Direccion
from restaurantes.forms import RestauranteCreateForm, RestauranteEditForm
# Create your views here.

@login_required(login_url='/account/login')
def rest_settings_create(request):
    if(request.user.profile.restaurante is not None):
        messages.error(request, "Ya has creado tu restaurante, ahora solo puedes editarla.")
        return redirect('cpanel_board')
    form = RestauranteCreateForm()
    if request.method == 'POST':
        form = RestauranteCreateForm(request.POST, request.FILES)
        if form.is_valid():
            rest = form.save()
            request.user.profile.restaurante = rest
            request.user.profile.save()
            messages.success(request, "¡Felicidades, has creado tu restaurante!")
            return redirect('cpanel_board')
        else:
            messages.error(request, "Los datos introducidos no son validos.")
    context = {'form':form}
    return render(request, 'CPSettingsRestaurante/create.html', context)

def rest_settings_update(request):
    if(request.user.profile.restaurante is None):
        return redirect('cpanel_board')
        
    if request.method == 'POST':
        cambios=None
        if None is not request.POST['nombre'].strip() is not '':
            request.user.profile.restaurante.nombre = request.POST['nombre'].strip()
            cambios=1

        if None is not request.POST['descr'].strip() is not '':
            request.user.profile.restaurante.nombre = request.POST['descr'].strip()
            cambios=1

        if None is not request.FILES.get('logo', None) is not '':
            request.user.profile.restaurante.logo = request.FILES['logo']
            cambios=1

        if None is not request.FILES.get('banner', None) is not '':
            request.user.profile.restaurante.banner = request.FILES['banner']
            cambios=1

        if cambios is not None:
            request.user.profile.restaurante.save()
            messages.success(request, "¡Cambios guardados con éxito!")

    rest = Restaurante.objects.get(pk=request.user.profile.restaurante.id)
    form = RestauranteEditForm(instance=rest)
    context = {'form':form}
    return render(request, 'CPSettingsRestaurante/update.html', context)

def rest_settings_view(request):
    return render(request, 'CPSettingsRestaurante/view.html')