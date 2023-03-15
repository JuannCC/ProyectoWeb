from django.urls import path
from ProyectowebApp import views
from . import views

urlpatterns = [
    path('',views.tienda, name='Tienda'),
]