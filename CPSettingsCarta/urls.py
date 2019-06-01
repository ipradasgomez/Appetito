from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.menu_settings_view, name="settings_menu_view"),    
    path('addCat/', views.menu_cat_create, name="settings_menu_addCat"),
    path('removeCat/', views.menu_cat_remove, name="settings_menu_removecat"),
    path('editCat/', views.menu_cat_edit, name="settings_menu_editCat"),
    path('addFood/<int:cat_id>/', views.menu_food_create, name="settings_menu_newfood"),
    path('removeFood/<int:food_id>/', views.menu_food_remove, name="settings_menu_removefood"),
]