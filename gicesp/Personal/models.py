from django.db import models
from datetime import datetime

# Imports desde mis modulos

from Servicios.models import Servicio

# Create your models here.

class Persona (models.Model):
    generos = (('M', 'Masculino'), ('F', 'Femenino'), )
    nombres = models.CharField('Nombres', max_length=50, help_text='Ingresar solo los nombres')
    apellidos = models.CharField('Apellidos', max_length=50, help_text='Ingresar solo los apellidos')
    apellido_casada = models.CharField('Apellido de Casada', max_length=50, blank=True, null=True, help_text='Ingresar solo los apellidos')
    genero = models.CharField('Género', max_length=1, choices=generos, default='F')
    fecha_nacimiento = models.DateField('Fecha de nacimiento', help_text='Ejemplo: 01/01/1991')

    """
    Funcion que calcula la edad cada persona según su fecha de nacimiento.
    El resultado de la fecha actual menos la fecha de nacimiento se dividirá dentro de 365.25 tomando en cuanta que cada 4 años 
    hay un día extra, ese día extra se dividirá dentro de 4 y el resultado se sumará a los 365 dias que tiene un año normal.
    """
    def edad (self) :
        edad = int((datetime.now().date() - self.fecha_nacimiento).days / 365.25)
        return '%s años' % edad

    #Función que une los nombres y los apellidos de las personas y retorna su nombre completo
    def nombrecompleto(self) :
        nombre = "{0} {1} de {2}"
        return nombre.format(self.nombres, self.apellidos, self.apellido_casada)

    #Función por defecto que retorna el nombre completa de las personas
    def __str__(self):
        return self.nombrecompleto()

    class Meta:
        abstract = True #El atributo abstract permite que la clase persona pueda ser usada para heredar a otra clase.
        unique_together = [('nombres','apellidos'),]

class Personal (Persona):
    funciones = (('A', 'Auxiliar de Enfermeria'), ('J', 'Enfermera Jefe de Servicio'), ('S', 'Supervisor de Enfermeria'))
    renglones = (('1', 'Renglón 011'), ('2', 'Renglón 182'))
    funcion = models.CharField('Función', max_length=1, choices=funciones, default='A')
    renglon = models.CharField('Renglón', max_length=1, choices=renglones, default='1')
    servicio = models.ForeignKey(Servicio, on_delete = models.CASCADE, verbose_name='Servicio asignado')
    estado = models.BooleanField('Estado', default=True)

    def __str__(self):
        return self.nombrecompleto()

    class Meta:
        db_table = 'personal'
        verbose_name = 'Personal'
        verbose_name_plural = 'Personal'
