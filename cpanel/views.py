from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from plans.models import Plan
# Create your views here.
@login_required(login_url='/account/login')
def cpanel_board(request):    
    context = {
        'nav_board': 'active',
        'higher_plans': Plan.objects.filter(pk__gt=request.user.profile.plan.id),
    }
    return render (request, 'cpanel/board.html', context)