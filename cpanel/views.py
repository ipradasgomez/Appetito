from django.shortcuts import render

# Create your views here.
def cpanel_board(request):
    return render (request, 'cpanel/board.html',  {'nav_board': 'active'})