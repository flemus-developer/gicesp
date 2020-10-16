from django.contrib import admin
from Personal.models import Personal
# Register your models here.

class PersonalAdmin(admin.ModelAdmin):
    readonly_fields = ['estado']
    search_fields = ['nombres', 'apellidos']
    list_filter = ['genero', 'funcion', 'servicio', 'estado']
    fields = (('nombres', 'apellidos', 'apellido_casada'), ('genero', 'fecha_nacimiento'), ('funcion', 'renglon', 'servicio'), 'estado')
    list_display = ['id', 'nombrecompleto', 'edad', 'funcion', 'renglon', 'servicio', 'estado']
    ordering = ['id'] #visualizaremos los datos ordenados por nombres

admin.site.register(Personal, PersonalAdmin)
