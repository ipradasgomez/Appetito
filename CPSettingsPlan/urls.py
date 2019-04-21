from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.plan_settings_index, name="settings_plan_idx"),
    path('pay/<int:plan_id>/', views.plan_settings_ascend, name="settings_plan_ascend"),
]