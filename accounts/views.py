from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.

def register(request):
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
                        messages.success(request, 'Felicidades, ya estás contectado')
                        return redirect('landing')
            else:
                messages.error(request, 'Las contraseñas no coinciden')
                return redirect('register')
        else:
            messages.error(request, 'Debes rellenar todos los campos')
            return redirect('register')
    else:    
        return render(request, 'accounts/register.html', {'nav_register':'active'})

def login(request):
    if request.method == 'POST':
        return redirect('login')
    else:
        return render(request, 'accounts/login.html', {'nav_login':'active'})

def logout(request):
    return redirect('landing')