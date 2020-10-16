from django.db import models
from django.contrib.auth import get_user_model
from Servicios.models import Servicio

User=get_user_model()

def getUsuario(request):
    usuario=request.user.first_name
    print(usuario)
    return usuario

# Create your models here.

class IndicadoresEnComun (models.Model):
    turnos = (('M', 'Mañana'), ('T', 'Tarde'), ('N', 'Noche'))
    fecha = models.DateField('Fecha', help_text='Fecha que se recolectaron los indicadores')
    servicio = models.ForeignKey(Servicio, on_delete = models.CASCADE, blank=True)
    turno = models.CharField('Turno', max_length=1, choices=turnos, default='F')
    accidentes = models.PositiveIntegerField('Accidentes intrahospitalarios', default=0)
    baño_esponja = models.PositiveIntegerField('Baños de esponja', default=0)
    caidas = models.PositiveIntegerField('Caídas de pacientes', default=0)
    cambios = models.PositiveIntegerField('Cambios de sondas', default=0)
    colocacion_correcta = models.PositiveIntegerField('Colocación de sondas Foley correctas', default=0)
    colocacion_incorrecta = models.PositiveIntegerField('Colocación de sondas Foley incorrectas', default=0)
    flebitis = models.PositiveIntegerField('Flebitis', default=0)
    prevenciones_itu = models.PositiveIntegerField('Prevención de infecciones por ITU por sonda vesical', default=0)
    quemaduras = models.PositiveIntegerField('Quemaduras por contacto', default=0)
    retiracion_puntos = models.PositiveIntegerField('Retiración de puntos', default=0)
    trato_digno = models.PositiveIntegerField('Trato digno', default=0)
    ulceras = models.PositiveIntegerField('Ulceras por presión', default=0)

    def __str__(self):
        cadena = '{0} {1}'
        return  cadena.format(self.fecha, self.turno)

    class Meta:
        abstract = True #El atributo abstract permite que la clase persona pueda ser usada para heredar a otra clase.
        unique_together = [('fecha','turno'),]

class IndicadoresCentral (IndicadoresEnComun):
    encargado = models.CharField('Encargado', max_length=250, blank=True)
    electro = models.PositiveIntegerField('Electrocardiogramas', default=0)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'indicador_central_equipos'
        verbose_name = 'Indicadores de Central de equipos'
        verbose_name_plural = 'Indicadores de Central de equipos'

class IndicadoresCirugias (IndicadoresEnComun):
    encargado = models.CharField('Encargado', max_length=250, blank=True)
    electro = models.PositiveIntegerField('Electrocardiogramas', default=0)
    yeso = models.PositiveIntegerField('Retiración de yesos', default=0)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'indicador_cirugias'
        verbose_name = 'Indicadores de Cirugías de hombre y de mujeres'
        verbose_name_plural = 'Indicadores de Cirugías de hombre y de mujeres'

class IndicadoresConsulta (IndicadoresEnComun):
    encargado = models.CharField('Encargado', max_length=250, blank=True)
    electro = models.PositiveIntegerField('Electrocardiogramas', default=0)
    yeso = models.PositiveIntegerField('Retiración de yesos', default=0)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'indicador_consulta_externa'
        verbose_name = 'Indicadores de Consulta externa'
        verbose_name_plural = 'Indicadores de Consulta externa'

class IndicadoresEmergencia (IndicadoresEnComun):
    encargado = models.CharField('Encargado', max_length=250, blank=True)
    atencion_partos = models.PositiveIntegerField('Atención de partos', default=0)
    partos_circulados = models.PositiveIntegerField('Partos_circulados', default=0)
    episiotomias = models.PositiveIntegerField('Episiotomías', default=0)
    baños_rn = models.PositiveIntegerField('Baños de recién nacidos', default=0)
    yeso = models.PositiveIntegerField('Retiración de yesos', default=0)
    electro = models.PositiveIntegerField('Electrocardiogramas', default=0)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'indicador_emergencia'
        verbose_name = 'Indicadores de Emergencia'
        verbose_name_plural = 'Indicadores de Emergencia'

class IndicadoresLabor (IndicadoresEnComun):
    encargado = models.CharField('Encargado', max_length=250, blank=True)
    atencion_partos = models.PositiveIntegerField('Atención de partos', default=0)
    partos_circulados = models.PositiveIntegerField('Partos_circulados', default=0)
    episiotomias = models.PositiveIntegerField('Episiotomías', default=0)
    cateteres = models.PositiveIntegerField('Catéteres umbilicales circulados', default=0)
    oxitocinas = models.PositiveIntegerField('Uso de oxitocinas en infusión', default=0)
    electro = models.PositiveIntegerField('Electrocardiogramas', default=0)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'indicador_labor_partos'
        verbose_name = 'Indicadores de Labor y partos'
        verbose_name_plural = 'Indicadores de Labor y partos'

class IndicadoresMaternidad (IndicadoresEnComun):
    encargado = models.CharField('Encargado', max_length=250, blank=True)
    atencion_partos = models.PositiveIntegerField('Atención de partos', default=0)
    partos_circulados = models.PositiveIntegerField('Partos_circulados', default=0)
    episiotomias = models.PositiveIntegerField('Episiotomías', default=0)
    cateteres = models.PositiveIntegerField('Catéteres umbilicales circulados', default=0)
    oxitocinas = models.PositiveIntegerField('Uso de oxitocinas en infusión', default=0)
    baños_rn = models.PositiveIntegerField('Baños de recién nacidos', default=0)
    electro = models.PositiveIntegerField('Electrocardiogramas', default=0)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'indicador_maternidad'
        verbose_name = 'Indicadores de Maternidad'
        verbose_name_plural = 'Indicadores de Maternidad'

class IndicadoresMedicinaH (IndicadoresEnComun):
    encargado = models.CharField('Encargado', max_length=250, blank=True)
    electro = models.PositiveIntegerField('Electrocardiogramas', default=0)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'indicador_medicina_hombres'
        verbose_name = 'Indicadores de Medicina de hombres'
        verbose_name_plural = 'Indicadores de Medicina de hombres'

class IndicadoresMedicinaM (IndicadoresEnComun):
    encargado = models.CharField('Encargado', max_length=250, blank=True)
    electro = models.PositiveIntegerField('Electrocardiogramas', default=0)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'indicador_medicina_mujeres'
        verbose_name = 'Indicadores de Medicina de mujeres'
        verbose_name_plural = 'Indicadores de Medicina de mujeres'

class IndicadoresNeonatos (IndicadoresEnComun):
    encargado = models.CharField('Encargado', max_length=250, blank=True)
    cateter_umbilical = models.PositiveIntegerField('Catéteres umbilicales circulados', default=0)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'indicador_neonatos'
        verbose_name = 'Indicadores de Neonatos'
        verbose_name_plural = 'Indicadores de Neonatos'

class IndicadoresPediatria (IndicadoresEnComun):
    encargado = models.CharField('Encargado', max_length=250, blank=True)
    cateter_umbilical = models.PositiveIntegerField('Catéteres umbilicales circulados', default=0)
    electro = models.PositiveIntegerField('Electrocardiogramas', default=0)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'indicador_pediatria'
        verbose_name = 'Indicadores de Pediatría'
        verbose_name_plural = 'Indicadores de Pediatría'

class IndicadoresSala (IndicadoresEnComun):
    encargado = models.CharField('Encargado', max_length=250, blank=True)
    electro = models.PositiveIntegerField('Electrocardiogramas', default=0)

    def __str__(self):
        return str(self.fecha)

    class Meta:
        db_table = 'indicador_sala_operaciones'
        verbose_name = 'Indicadores de Sala de operaciones'
        verbose_name_plural = 'Indicadores de Sala de operaciones'
