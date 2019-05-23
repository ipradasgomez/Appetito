from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from plans.models import Plan
from django.contrib import messages
# Create your views here.
@login_required(login_url='/account/login')
def cpanel_board(request):
    if request.user.profile.restaurante is None:
        messages.success(request, "¡Ahora que tienes cuenta debes crear tu empresa!")
        return redirect('settings_rest_create')
    context = {
        'nav_board': 'active',
        'higher_plans': Plan.objects.filter(pk__gt=request.user.profile.plan.id),
    }
    return render (request, 'cpanel/board.html', context)