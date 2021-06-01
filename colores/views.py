from django.shortcuts import render
from .models import Color
from django.conf import settings 
# Create your views here.

def colores(request):
    if request.method == "POST" and 'imagen' in request.FILES:
        nombre = request.POST.get("nombre")
        imagen = request.FILES.get("imagen")
        # imagen = request.FILES
        color = Color(nombre=nombre, imagen=imagen)
        color.save()
    return render(request, 'colores.html')
