# Generated by Django 3.0 on 2020-10-13 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Servicios', '0001_initial'),
        ('Personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('supervisor', models.CharField(blank=True, max_length=250, verbose_name='Supervisor')),
                ('personal', models.ForeignKey(help_text='Persona a la que se le esta levantando un reporte', on_delete=django.db.models.deletion.CASCADE, to='Personal.Personal')),
                ('servicio', models.ForeignKey(help_text='Servicio donde se cometió una falta', on_delete=django.db.models.deletion.CASCADE, to='Servicios.Servicio')),
            ],
            options={
                'verbose_name': 'Reporte',
                'verbose_name_plural': 'Reportes',
                'db_table': 'reporte',
            },
        ),
    ]
