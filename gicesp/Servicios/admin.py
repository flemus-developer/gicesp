from django.contrib import admin
from Servicios.models import Servicio
# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['id', 'nombre']
    ordering = ['id'] #visualizaremos los datos ordenados por nombres

admin.site.register(Servicio, ServicioAdmin)
