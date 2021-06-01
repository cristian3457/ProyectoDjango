from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
# Create your views here.

def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        mensaje = request.POST.get("mensaje")
        asunto = request.POST.get("asunto")
        correo =  EmailMessage(asunto, "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre, email, mensaje),
        "", ['s16120279@alumnos.itsur.edu.mx'], reply_to=[email])
        try:
            correo.send()
            return redirect("/contacto/?valido")
        except:
            return redirect("/contacto/?novalido")
    return render(request,'contacto.html')