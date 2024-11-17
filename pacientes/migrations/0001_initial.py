# Generated by Django 4.2 on 2024-11-17 03:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=12, unique=True)),
                ('patologia', models.CharField(max_length=200)),
                ('observaciones', models.TextField(blank=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('estado', models.CharField(choices=[('en_proceso', 'En Proceso'), ('terminado', 'Terminado'), ('no_terminado', 'No Terminado')], max_length=20)),
                ('kinesiologo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pacientes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('completada', models.BooleanField(default=False)),
                ('notas', models.TextField(blank=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sesiones', to='pacientes.paciente')),
            ],
        ),
    ]