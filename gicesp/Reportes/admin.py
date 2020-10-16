from django.contrib import admin
from Reportes.models import Reporte

# Register your models here.

class ReporteAdmin(admin.ModelAdmin):
    readonly_fields = ['supervisor']
    search_fields = ['supervisor', 'personal__nombres', 'personal__apellidos']
    list_filter = ['fecha', 'servicio']
    list_display = ['fecha', 'servicio', 'personal', 'descripcion', 'supervisor']
    ordering = ['fecha'] #visualizaremos los datos ordenados por nombres

    def save_model(self, request, obj, form, change):
        usuario='{0} {1}'
        obj.supervisor=usuario.format(request.user.first_name, request.user.last_name)
        obj.save()

admin.site.register(Reporte, ReporteAdmin)
