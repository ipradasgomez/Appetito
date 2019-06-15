from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from django.contrib import messages
from plans.models import Plan
# Create your views here.

@login_required(login_url='/account/login')
def plan_settings_index(request):
    context = {
        'higher_plans': Plan.objects.filter(pk__gt=request.user.profile.plan.id),
        'plans':Plan.objects.all()
    }
    return render(request, 'CPSettingsPlan/plan_settings_index.html', context)

@login_required(login_url='/account/login')
def plan_settings_ascend(request, plan_id=1):
    context = {}
    if Plan.objects.filter(pk=plan_id).exists():
        plan = Plan.objects.filter(pk=plan_id).first()
        if (plan.id > request.user.profile.plan.id):
            if request.method == 'POST':
                if payment_is_valid():
                    prof = Profile.objects.get(user_id=request.user.id)
                    prof.plan_id = plan.id
                    prof.save()
                    messages.success(request, "¡Felicidades, ahora perteneces al Plan {}".format(plan.nombre))
                    return redirect('settings_plan_idx')
                else:
                    context['err'] = "Error: Ha sido imposible realizar el pago."                          
            context['plan'] = plan
        else:
            context['err'] = "Error: Actualmente tu subscripción es igual o superior a la solicitada." 
    else:
        context['err'] = "Error: No ha sido posible encontrar la subscripción solicitada."        
    
    return render(request, 'CPSettingsPlan/plan_settings_ascend.html', context)

def payment_is_valid():
    return True