from django.urls import path

from . import views

urlpatterns = [
    path('modelo1/', views.modelo1, name='Modelo1'),
    path('modelo2/', views.modelo2, name='Modelo2'),
]
