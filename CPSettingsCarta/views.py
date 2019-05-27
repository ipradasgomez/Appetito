from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/account/login')
def menu_settings_view(request):
    return render(request, 'CPSettingsCarta/index.html')

@login_required(login_url='/account/login')
def menu_cat_create(request):
    pass

@login_required(login_url='/account/login')
def menu_cat_remove(request):
    pass

@login_required(login_url='/account/login')
def menu_food_create(request):
    pass

@login_required(login_url='/account/login')
def menu_food_remove(request):
    pass