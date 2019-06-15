from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from restaurantes.models import Direccion
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.

@login_required(login_url='/account/login')
def location_settings_view(request):
    if request.user.profile.restaurante is None:
        messages.success(request, "Antes de editar tus parámetros debes crear tu empresa.")
        return redirect('settings_rest_create')
    return render(request, 'CPSettingsLocations/view.html')

@login_required(login_url='/account/login')
def location_settings_create(request):
    if request.user.profile.restaurante is None:
        messages.success(request, "Antes de editar tus parámetros debes crear tu empresa.")
        return redirect('settings_rest_create')
    if(request.POST):
        if(request.user.profile.restaurante.direcciones.all().count() < request.user.profile.plan.max_empresas or request.user.profile.plan.max_empresas is 0):
            dir = Direccion.objects.create(direccion=request.POST['dir'], lat=request.POST['lat'], long=request.POST['long'], restaurante_id=request.user.profile.restaurante.id)
            dir.save()
            messages.success(request, "Dirección creada con éxito.")
        else:
            messages.success(request, "Has alcanzado el límite máximo de direcciones.")
        return redirect('settings_loc_view')

    context= None
    return render(request, 'CPSettingsLocations/create.html', context)

@login_required(login_url='/account/login')
def location_settings_delete(request, location_id):
    if request.user.profile.restaurante is None:
        messages.success(request, "Antes de editar tus parámetros debes crear tu empresa.")
        return redirect('settings_rest_create')
    dir = Direccion.objects.get(id=location_id)
    dir.delete()
    messages.success(request, "Dirección eliminada.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))