from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/account/login')
def cpanel_board(request):
    return render (request, 'cpanel/board.html',  {'nav_board': 'active'})