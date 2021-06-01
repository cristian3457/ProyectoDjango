from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
# Create your views here.

def iniciarSesion(request):
    if request.method == "POST":
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        # existe = User.objects.check(usuario = usuario, password = password)
        # return redirect('/login/?datos')
        user = authenticate(username=usuario, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect("/login/?novalido")
         
    return render(request,'login.html')

def registro(request):
    if request.method == "POST":
        usuario = request.POST.get('username')
        password = request.POST.get('password')
        nombre = request.POST.get('first_name')
        apellidos = request.POST.get('last_name')
        email = request.POST.get('email')
        user = User.objects.create_user(usuario, email, password)
        user.first_name = nombre
        user.last_name = apellidos
        user.save()
        user = authenticate(username=usuario, password=password)
        if user is not None:
            login(request, user)
        return redirect('/')
    return render(request,'registro.html')

def cerrarSesion(request):
    logout(request)
    return redirect('/')