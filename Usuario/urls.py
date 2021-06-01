from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.iniciarSesion, name="Login"),
    path('registro/', views.registro, name="Registro"),
    path('cerrarSesion/', views.cerrarSesion, name="Logout"),
]