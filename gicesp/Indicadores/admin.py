from django.contrib import admin
from Indicadores.models import *
# Register your models here.

class IndicadoresCentralAdmin(admin.ModelAdmin):
    readonly_fields = ['encargado']
    search_fields = ['encargado']
    list_filter = ['fecha', 'turno']
    list_display = ['fecha', 'turno', 'encargado']
    ordering = ['fecha'] #visualizaremos los datos ordenados por nombres

    def save_model(self, request, obj, form, change):
        usuario='{0} {1}'
        obj.encargado=usuario.format(request.user.first_name, request.user.last_name)
        obj.save()

class IndicadoresCirugiasAdmin(admin.ModelAdmin):
    readonly_fields = ['encargado']
    search_fields = ['encargado']
    list_filter = ['fecha', 'turno']
    list_display = ['fecha', 'turno', 'encargado']
    ordering = ['fecha'] #visualizaremos los datos ordenados por nombres

    def save_model(self, request, obj, form, change):
        usuario='{0} {1}'
        obj.encargado=usuario.format(request.user.first_name, request.user.last_name)
        obj.save()

class IndicadoresConsultaAdmin(admin.ModelAdmin):
    readonly_fields = ['encargado']
    search_fields = ['encargado']
    list_filter = ['fecha', 'turno']
    list_display = ['fecha', 'turno', 'encargado']
    ordering = ['fecha'] #visualizaremos los datos ordenados por nombres

    def save_model(self, request, obj, form, change):
        usuario='{0} {1}'
        obj.encargado=usuario.format(request.user.first_name, request.user.last_name)
        obj.save()

class IndicadoresEmergenciaAdmin(admin.ModelAdmin):
    readonly_fields = ['encargado']
    search_fields = ['encargado']
    list_filter = ['fecha', 'turno']
    list_display = ['fecha', 'turno', 'encargado']
    ordering = ['fecha'] #visualizaremos los datos ordenados por nombres

    def save_model(self, request, obj, form, change):
        usuario='{0} {1}'
        obj.encargado=usuario.format(request.user.first_name, request.user.last_name)
        obj.save()

class IndicadoresLaborAdmin(admin.ModelAdmin):
    readonly_fields = ['encargado']
    search_fields = ['encargado']
    list_filter = ['fecha', 'turno']
    list_display = ['fecha', 'turno', 'encargado']
    ordering = ['fecha'] #visualizaremos los datos ordenados por nombres

    def save_model(self, request, obj, form, change):
        usuario='{0} {1}'
        obj.encargado=usuario.format(request.user.first_name, request.user.last_name)
        obj.save()

class IndicadoresMaternidadAdmin(admin.ModelAdmin):
    readonly_fields = ['encargado']
    search_fields = ['encargado']
    list_filter = ['fecha', 'turno']
    list_display = ['fecha', 'turno', 'encargado']
    ordering = ['fecha'] #visualizaremos los datos ordenados por nombres

    def save_model(self, request, obj, form, change):
        usuario='{0} {1}'
        obj.encargado=usuario.format(request.user.first_name, request.user.last_name)
        obj.save()

class IndicadoresMedicinaHAdmin(admin.ModelAdmin):
    readonly_fields = ['encargado']
    search_fields = ['encargado']
    list_filter = ['fecha', 'turno']
    list_display = ['fecha', 'turno', 'encargado']
    ordering = ['fecha'] #visualizaremos los datos ordenados por nombres

    def save_model(self, request, obj, form, change):
        usuario='{0} {1}'
        obj.encargado=usuario.format(request.user.first_name, request.user.last_name)
        obj.save()

class IndicadoresMedicinaMAdmin(admin.ModelAdmin):
    readonly_fields = ['encargado']
    search_fields = ['encargado']
    list_filter = ['fecha', 'turno']
    list_display = ['fecha', 'turno', 'encargado']
    ordering = ['fecha'] #visualizaremos los datos ordenados por nombres

    def save_model(self, request, obj, form, change):
        usuario='{0} {1}'
        obj.encargado=usuario.format(request.user.first_name, request.user.last_name)
        obj.save()

class IndicadoresNeonatosAdmin(admin.ModelAdmin):
    readonly_fields = ['encargado']
    search_fields = ['encargado']
    list_filter = ['fecha', 'turno']
    list_display = ['fecha', 'turno', 'encargado']
    ordering = ['fecha'] #visualizaremos los datos ordenados por nombres

    def save_model(self, request, obj, form, change):
        usuario='{0} {1}'
        obj.encargado=usuario.format(request.user.first_name, request.user.last_name)
        obj.save()

class IndicadoresPediatriaAdmin(admin.ModelAdmin):
    readonly_fields = ['encargado']
    search_fields = ['encargado']
    list_filter = ['fecha', 'turno']
    list_display = ['fecha', 'turno', 'encargado']
    ordering = ['fecha'] #visualizaremos los datos ordenados por nombres

    def save_model(self, request, obj, form, change):
        usuario='{0} {1}'
        obj.encargado=usuario.format(request.user.first_name, request.user.last_name)
        obj.save()

class IndicadoresSalaAdmin(admin.ModelAdmin):
    readonly_fields = ['encargado']
    search_fields = ['encargado']
    list_filter = ['fecha', 'turno']
    list_display = ['fecha', 'turno', 'encargado']
    ordering = ['fecha'] #visualizaremos los datos ordenados por nombres

    def save_model(self, request, obj, form, change):
        usuario='{0} {1}'
        obj.encargado=usuario.format(request.user.first_name, request.user.last_name)
        obj.save()

admin.site.register(IndicadoresCentral, IndicadoresCentralAdmin)
admin.site.register(IndicadoresCirugias, IndicadoresCirugiasAdmin)
admin.site.register(IndicadoresConsulta, IndicadoresConsultaAdmin)
admin.site.register(IndicadoresEmergencia, IndicadoresEmergenciaAdmin)
admin.site.register(IndicadoresLabor, IndicadoresLaborAdmin)
admin.site.register(IndicadoresMaternidad, IndicadoresMaternidadAdmin)
admin.site.register(IndicadoresMedicinaH, IndicadoresMedicinaHAdmin)
admin.site.register(IndicadoresMedicinaM, IndicadoresMedicinaMAdmin)
admin.site.register(IndicadoresNeonatos, IndicadoresNeonatosAdmin)
admin.site.register(IndicadoresPediatria, IndicadoresPediatriaAdmin)
admin.site.register(IndicadoresSala, IndicadoresSalaAdmin)
