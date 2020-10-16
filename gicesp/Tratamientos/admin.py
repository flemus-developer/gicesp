from django.contrib import admin
from Tratamientos.models import *

# Register your models here.

class TratamientosCentralAdmin(admin.ModelAdmin):
    readonly_fields = ['servicio', 'encargado']
    search_fields = ['encargado']
    list_filter = ['fecha', 'turno', 'servicio']
    list_display = ['fecha', 'turno', 'encargado', 'servicio']
    ordering = ['fecha'] #visualizaremos los datos ordenados por nombres

    def save_model(self, request, obj, form, change):
        from Servicios.models import Servicio
        serv = Servicio.objects.get(id=1)
        usuario='{0} {1}'
        obj.servicio=serv
        obj.encargado=usuario.format(request.user.first_name, request.user.last_name)
        obj.save()

class TratamientosCirugiasAdmin(admin.ModelAdmin):
    readonly_fields = ['servicio', 'encargado']
    search_fields = ['encargado']
    list_filter = ['fecha', 'turno', 'servicio']
    list_display = ['fecha', 'turno', 'encargado', 'servicio']
    ordering = ['fecha'] #visualizaremos los datos ordenados por nombres

    def save_model(self, request, obj, form, change):
        from Servicios.models import Servicio
        serv = Servicio.objects.get(id=2)
        usuario='{0} {1}'
        obj.servicio=serv
        obj.encargado=usuario.format(request.user.first_name, request.user.last_name)
        obj.save()

class TratamientosConsultaAdmin(admin.ModelAdmin):
    readonly_fields = ['servicio', 'encargado']
    search_fields = ['encargado']
    list_filter = ['fecha', 'turno', 'servicio']
    list_display = ['fecha', 'turno', 'encargado', 'servicio']
    ordering = ['fecha'] #visualizaremos los datos ordenados por nombres

    def save_model(self, request, obj, form, change):
        from Servicios.models import Servicio
        serv = Servicio.objects.get(id=3)
        usuario='{0} {1}'
        obj.servicio=serv
        obj.encargado=usuario.format(request.user.first_name, request.user.last_name)
        obj.save()

class TratamientosEmergenciaAdmin(admin.ModelAdmin):
    readonly_fields = ['servicio', 'encargado']
    search_fields = ['encargado']
    list_filter = ['fecha', 'turno', 'servicio']
    list_display = ['fecha', 'turno', 'encargado', 'servicio']
    ordering = ['fecha'] #visualizaremos los datos ordenados por nombres

    def save_model(self, request, obj, form, change):
        from Servicios.models import Servicio
        serv = Servicio.objects.get(id=4)
        usuario='{0} {1}'
        obj.servicio=serv
        obj.encargado=usuario.format(request.user.first_name, request.user.last_name)
        obj.save()

class TratamientosLaborAdmin(admin.ModelAdmin):
    readonly_fields = ['servicio', 'encargado']
    search_fields = ['encargado']
    list_filter = ['fecha', 'turno', 'servicio']
    list_display = ['fecha', 'turno', 'encargado', 'servicio']
    ordering = ['fecha'] #visualizaremos los datos ordenados por nombres

    def save_model(self, request, obj, form, change):
        from Servicios.models import Servicio
        serv = Servicio.objects.get(id=5)
        usuario='{0} {1}'
        obj.servicio=serv
        obj.encargado=usuario.format(request.user.first_name, request.user.last_name)
        obj.save()

class TratamientosMaternidadAdmin(admin.ModelAdmin):
    readonly_fields = ['servicio', 'encargado']
    search_fields = ['encargado']
    list_filter = ['fecha', 'turno', 'servicio']
    list_display = ['fecha', 'turno', 'encargado', 'servicio']
    ordering = ['fecha'] #visualizaremos los datos ordenados por nombres

    def save_model(self, request, obj, form, change):
        from Servicios.models import Servicio
        serv = Servicio.objects.get(id=6)
        usuario='{0} {1}'
        obj.servicio=serv
        obj.encargado=usuario.format(request.user.first_name, request.user.last_name)
        obj.save()

class TratamientosMedicinaHAdmin(admin.ModelAdmin):
    readonly_fields = ['servicio', 'encargado']
    search_fields = ['encargado']
    list_filter = ['fecha', 'turno', 'servicio']
    list_display = ['fecha', 'turno', 'encargado', 'servicio']
    ordering = ['fecha'] #visualizaremos los datos ordenados por nombres

    def save_model(self, request, obj, form, change):
        from Servicios.models import Servicio
        serv = Servicio.objects.get(id=7)
        usuario='{0} {1}'
        obj.servicio=serv
        obj.encargado=usuario.format(request.user.first_name, request.user.last_name)
        obj.save()

class TratamientosMedicinaMAdmin(admin.ModelAdmin):
    readonly_fields = ['servicio', 'encargado']
    search_fields = ['encargado']
    list_filter = ['fecha', 'turno', 'servicio']
    list_display = ['fecha', 'turno', 'encargado', 'servicio']
    ordering = ['fecha'] #visualizaremos los datos ordenados por nombres

    def save_model(self, request, obj, form, change):
        from Servicios.models import Servicio
        serv = Servicio.objects.get(id=8)
        usuario='{0} {1}'
        obj.servicio=serv
        obj.encargado=usuario.format(request.user.first_name, request.user.last_name)
        obj.save()

class TratamientosNeonatosAdmin(admin.ModelAdmin):
    readonly_fields = ['servicio', 'encargado']
    search_fields = ['encargado']
    list_filter = ['fecha', 'turno', 'servicio']
    list_display = ['fecha', 'turno', 'encargado', 'servicio']
    ordering = ['fecha'] #visualizaremos los datos ordenados por nombres

    def save_model(self, request, obj, form, change):
        from Servicios.models import Servicio
        serv = Servicio.objects.get(id=9)
        usuario='{0} {1}'
        obj.servicio=serv
        obj.encargado=usuario.format(request.user.first_name, request.user.last_name)
        obj.save()

class TratamientosPediatriaAdmin(admin.ModelAdmin):
    readonly_fields = ['servicio', 'encargado']
    search_fields = ['encargado']
    list_filter = ['fecha', 'turno', 'servicio']
    list_display = ['fecha', 'turno', 'encargado', 'servicio']
    ordering = ['fecha'] #visualizaremos los datos ordenados por nombres

    def save_model(self, request, obj, form, change):
        from Servicios.models import Servicio
        serv = Servicio.objects.get(id=10)
        usuario='{0} {1}'
        obj.servicio=serv
        obj.encargado=usuario.format(request.user.first_name, request.user.last_name)
        obj.save()

class TratamientosSalaAdmin(admin.ModelAdmin):
    readonly_fields = ['servicio', 'encargado']
    search_fields = ['encargado']
    list_filter = ['fecha', 'turno', 'servicio']
    list_display = ['fecha', 'turno', 'encargado', 'servicio']
    ordering = ['fecha'] #visualizaremos los datos ordenados por nombres

    def save_model(self, request, obj, form, change):
        from Servicios.models import Servicio
        serv = Servicio.objects.get(id=11)
        usuario='{0} {1}'
        obj.servicio=serv
        obj.encargado=usuario.format(request.user.first_name, request.user.last_name)
        obj.save()

admin.site.register(TratamientosCentral, TratamientosCentralAdmin)
admin.site.register(TratamientosCirugias, TratamientosCirugiasAdmin)
admin.site.register(TratamientosConsulta, TratamientosConsultaAdmin)
admin.site.register(TratamientosEmergencia, TratamientosEmergenciaAdmin)
admin.site.register(TratamientosLabor, TratamientosLaborAdmin)
admin.site.register(TratamientosMaternidad, TratamientosMaternidadAdmin)
admin.site.register(TratamientosMedicinaH, TratamientosMedicinaHAdmin)
admin.site.register(TratamientosMedicinaM, TratamientosMedicinaMAdmin)
admin.site.register(TratamientosNeonatos, TratamientosNeonatosAdmin)
admin.site.register(TratamientosPediatria, TratamientosPediatriaAdmin)
admin.site.register(TratamientosSala, TratamientosSalaAdmin)
