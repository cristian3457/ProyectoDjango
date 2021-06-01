import Usuario
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Alimento(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    imagen =  models.ImageField(upload_to="alimentos")
    descripcion = models.TextField()
    disponible = models.BooleanField(default=True)

    class Meta:
        verbose_name ='alimento'
        verbose_name_plural ='alimentos'
    
    def __str__(self):
        return self.nombre + ' ----->  '+ str(self.precio)

class Reservacion(models.Model):
    fecha = models.CharField(max_length=100)
    hora = models.CharField(max_length=20)
    usuario =  models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name ='reservación'
        verbose_name_plural ='reservaciones'
    
    def __str__(self):
        return str(self.fecha)



