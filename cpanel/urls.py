from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cpanel_board, name="cpanel_board"),
    path('settings/plan/', include('CPSettingsPlan.urls')),
]