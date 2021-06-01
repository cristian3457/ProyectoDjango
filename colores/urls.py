from django.urls import path
from . import views

urlpatterns = [
    path('colores/', views.colores, name="Colores"),
]