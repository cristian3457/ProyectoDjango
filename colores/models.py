from django.db import models

# Create your models here.

class Color(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="colores", blank=True, null = True)