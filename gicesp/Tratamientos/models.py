from django.db import models
from Servicios.models import Servicio

# Create your models here.

class Tratamientos (models.Model):
    turnos = (('M', 'Mañana'), ('T', 'Tarde'), ('N', 'Noche'))
    fecha = models.DateField('Fecha', help_text='Fecha que se recolectaron los tratamientos')
    turno = models.CharField('Turno', max_length=1, choices=turnos, default='F')
    admon_oxi = models.PositiveIntegerField('Administraciones de oxígeno', default=0)
    arreglos = models.PositiveIntegerField('Arreglo de unidades', default=0)
    canalizaciones = models.PositiveIntegerField('Canalizaciones', default=0)
    curaciones = models.PositiveIntegerField('Curaciones', default=0)
    hipodermia = models.PositiveIntegerField('Hipodermias', default=0)
    limpieza_unidad = models.PositiveIntegerField('Limpieza de unidades', default=0)
    traslados_ekg = models.PositiveIntegerField('Traslados de pacientes a electrocardiograma', default=0)
    traslados_rx = models.PositiveIntegerField('Traslados de pacientes a rayos X', default=0)
    nebulizaciones = models.PositiveIntegerField('Nebulizaciones', default=0)
    peq_cirugias = models.PositiveIntegerField('Pequeñas cirugias', default=0)
    recolect_muestras = models.PositiveIntegerField('Recolecciones de muestras', default=0)
    transfusiones = models.PositiveIntegerField('Transfusiones', default=0)

    def __str__(self):
        cadena = '{0} {1}'
        return  cadena.format(self.fecha, self.turno)

    class Meta:
        abstract = True
        unique_together = [('fecha','turno','servicio'),]

class TratamientosCentral (Tratamientos):
    servicio = models.ForeignKey(Servicio, on_delete = models.CASCADE, blank=True)
    encargado = models.CharField('Encargado', max_length=250, blank=True)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'tratamiento_central'
        verbose_name = 'Tratamientos de Central de equipos'
        verbose_name_plural = 'Tratamientos de Central de equipos'

class TratamientosCirugias(Tratamientos):
    servicio = models.ForeignKey(Servicio, on_delete = models.CASCADE, blank=True)
    encargado = models.CharField('Encargado', max_length=250, blank=True)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'tratamiento_cirugias'
        verbose_name = 'Tratamientos de Cirugías de hombre y de mujeres'
        verbose_name_plural = 'Tratamientos de Cirugías de hombre y de mujeres'

class TratamientosConsulta(Tratamientos):
    servicio = models.ForeignKey(Servicio, on_delete = models.CASCADE, blank=True)
    encargado = models.CharField('Encargado', max_length=250, blank=True)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'tratamiento_consulta_externa'
        verbose_name = 'Tratamientos de Consulta externa'
        verbose_name_plural = 'Tratamientos de Consulta externa'

class TratamientosEmergencia(Tratamientos):
    servicio = models.ForeignKey(Servicio, on_delete = models.CASCADE, blank=True)
    encargado = models.CharField('Encargado', max_length=250, blank=True)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'tratamiento_emergencia'
        verbose_name = 'Tratamientos de Emergencia'
        verbose_name_plural = 'Tratamientos de Emergencia'

class TratamientosLabor(Tratamientos):
    servicio = models.ForeignKey(Servicio, on_delete = models.CASCADE, blank=True)
    encargado = models.CharField('Encargado', max_length=250, blank=True)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'tratamiento_labor'
        verbose_name = 'Tratamientos de Labor y partos'
        verbose_name_plural = 'Tratamientos de Labor y partos'

class TratamientosMaternidad(Tratamientos):
    servicio = models.ForeignKey(Servicio, on_delete = models.CASCADE, blank=True)
    encargado = models.CharField('Encargado', max_length=250, blank=True)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'tratamiento_maternidad'
        verbose_name = 'Tratamientos de Maternidad'
        verbose_name_plural = 'Tratamientos de Maternidad'

class TratamientosMedicinaH(Tratamientos):
    servicio = models.ForeignKey(Servicio, on_delete = models.CASCADE, blank=True)
    encargado = models.CharField('Encargado', max_length=250, blank=True)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'tratamiento_medicina_hombres'
        verbose_name = 'Tratamientos de Medicina de hombres'
        verbose_name_plural = 'Tratamientos de Medicina de hombres'

class TratamientosMedicinaM(Tratamientos):
    servicio = models.ForeignKey(Servicio, on_delete = models.CASCADE, blank=True)
    encargado = models.CharField('Encargado', max_length=250, blank=True)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'tratamiento_medicina_mujeres'
        verbose_name = 'Tratamientos de Medicina de mujeres'
        verbose_name_plural = 'Tratamientos de Medicina de mujeres'

class TratamientosNeonatos(Tratamientos):
    servicio = models.ForeignKey(Servicio, on_delete = models.CASCADE, blank=True)
    encargado = models.CharField('Encargado', max_length=250, blank=True)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'tratamiento_neonatos'
        verbose_name = 'Tratamientos de Neonatos'
        verbose_name_plural = 'Tratamientos de Neonatos'

class TratamientosPediatria(Tratamientos):
    servicio = models.ForeignKey(Servicio, on_delete = models.CASCADE, blank=True)
    encargado = models.CharField('Encargado', max_length=250, blank=True)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'tratamiento_pediatria'
        verbose_name = 'Tratamientos de Pediatria'
        verbose_name_plural = 'Tratamientos de Pediatria'

class TratamientosSala(Tratamientos):
    servicio = models.ForeignKey(Servicio, on_delete = models.CASCADE, blank=True)
    encargado = models.CharField('Encargado', max_length=250, blank=True)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'tratamiento_sala'
        verbose_name = 'Tratamientos de Sala de operaciones'
        verbose_name_plural = 'Tratamientos de Sala de operaciones'
