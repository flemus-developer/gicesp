from django.db import models

# Create your models here.

class Servicio (models.Model):
    nombre = models.CharField('Nombre del Servicio', unique=True, max_length=50, help_text='Ej. Pediatría, Neonatos, Labor y Partos, etc.')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'servicio'
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
