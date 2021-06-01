from django.http import request
from django.shortcuts import redirect, render
from .models import Alimento, Reservacion
# Create your views here.

def menu(request):
    alimentos = Alimento.objects.all()
    return render(request,'menu.html',{'alimentos':alimentos})

def reservar(request):
    if request.method == "POST":
        fecha = "1 de Junio de 2021"
        hora = "17:58"
        usuario = request.POST.get("id_usuario")
        reservacion = Reservacion(fecha, hora,usuario)
        reservacion.save()
    return render(request,'menu.html')