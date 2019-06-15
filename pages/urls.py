from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
    path('restaurante/<int:id>', views.restaurante, name='ver_restaurante'),
    path('restaurante/pdf/<int:id>', views.respdf, name='restaurante_pdf'),
]
