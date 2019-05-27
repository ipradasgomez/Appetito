from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cpanel_board, name="cpanel_board"),
    path('settings/plan/', include('CPSettingsPlan.urls')),
    path('settings/rest/', include('CPSettingsRestaurante.urls')),
    path('settings/locations/', include('CPSettingsLocations.urls')),
    path('settings/menu/', include('CPSettingsCarta.urls')),
]