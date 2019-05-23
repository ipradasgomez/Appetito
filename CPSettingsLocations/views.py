from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/account/login')
def location_settings_view(request):
    context= None
    return render(request, 'CPSettingsLocations/view.html', context)

@login_required(login_url='/account/login')
def location_settings_create(request):
    context= None
    return render(request, 'CPSettingsLocations/create.html', context)

@login_required(login_url='/account/login')
def location_settings_delete(request):
    pass