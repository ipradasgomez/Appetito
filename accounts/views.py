from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def card_token(request):
    return HttpResponse(status=200)

def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['user']
            mail = request.POST['mail']
            password = request.POST['pass']
            repass = request.POST['repass']

            #Check if all
            if(username and mail and password and repass):
                #Check Pass
                if(password == repass):
                    #Check if user exists
                    if User.objects.filter(username=username).exists():
                        messages.error(request, 'El nombre de usuario no está disponible')
                        return redirect('register')
                    else:
                        #Check Email
                        if User.objects.filter(email=mail).exists():
                            messages.error(request, 'El e-mail ya se encuentra en uso.')
                            return redirect('register')
                        else:
                            user = User.objects.create_user(username=username, password=repass, email=mail, first_name='', last_name='')
                            #Log despues de registrar
                            auth.login(request, user)
                            request.session.set_expiry(0)
                            messages.success(request, '¡Bienvenido a Appetito! Este es tu panel de control... ¡Disfrutalo!')
                            return redirect('board')
                else:
                    messages.error(request, 'Las contraseñas no coinciden')
                    return redirect('register')
            else:
                messages.error(request, 'Debes rellenar todos los campos')
                return redirect('register')
        else:    
            return render(request, 'accounts/register.html', {'nav_register':'active'})
    else:
        return redirect('landing')

def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['pass']
            #Logueamos
            user = auth.authenticate(username=username, password=password)
            #Comprobamos
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Te has logueado correctamente')
                return redirect('board')
            else:            
                messages.error(request, 'El usuario o la clave no son correctos')
                return redirect('login')
        else:
            return render(request, 'accounts/login.html', {'nav_login':'active'})
    else:
        return redirect('landing')

def logout(request):
    if request.user.is_authenticated and request.method == 'POST':
            auth.logout(request)
            messages.success(request, 'Te has desconectado correctamente')
            return redirect('landing')