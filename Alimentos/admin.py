from django.contrib import admin
from django.contrib.admin.sites import site
from .models import Alimento, Reservacion
# Register your models here.

class ReservacionAdmin(admin.ModelAdmin):
    list_display = ("usuario", "fecha", "hora")

admin.site.register(Alimento)
admin.site.register(Reservacion, ReservacionAdmin)