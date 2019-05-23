from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.rest_settings_create, name="settings_rest_create"),
    path('update', views.rest_settings_update, name="settings_rest_update"),
    path('view', views.rest_settings_update, name="settings_rest_view"),
]