from django.urls import path
from . import views

urlpatterns = [
    path('', views.flappyCat, name='flappyCat'),
]