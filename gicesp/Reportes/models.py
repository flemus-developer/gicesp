from django.db import models
from Personal.models import Personal
from Servicios.models import Servicio

# Create your models here.

class Reporte (models.Model):
    fecha = models.DateField(auto_now_add=True)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, help_text='Servicio donde se cometió una falta')
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE, help_text='Persona a la que se le esta levantando un reporte')
    descripcion = models.TextField('Descripción')
    supervisor = models.CharField('Supervisor', max_length=250, blank=True)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'reporte'
        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'
