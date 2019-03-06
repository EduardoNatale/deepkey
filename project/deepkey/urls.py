from django.urls import path

from . import views

urlpatterns = [
    path('', views.deepkey, name='DeepKey'),
]
