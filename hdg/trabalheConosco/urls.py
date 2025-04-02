from django.urls import path
from . import views

urlpatterns = [
    path('', views.trabalheConosco, name='trabalheConosco'),
]