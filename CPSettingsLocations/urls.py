from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.location_settings_view, name="settings_loc_view"),
    path('create', views.location_settings_create, name="settings_loc_create"),
    path('delete/<int:location_id>', views.location_settings_delete, name="settings_loc_delete"),
]