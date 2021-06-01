from django.contrib import admin
from .models import Color
# Register your models here.

class ColorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "imagen")
    
admin.site.register(Color, ColorAdmin)