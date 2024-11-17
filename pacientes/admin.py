from django.contrib import admin
from .models import Paciente, Sesion

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'rut', 'estado', 'kinesiologo')
    list_filter = ('estado', 'kinesiologo')
    search_fields = ('nombre', 'apellido', 'rut')

@admin.register(Sesion)
class SesionAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha', 'completada')
    list_filter = ('completada', 'fecha')
    search_fields = ('paciente__nombre', 'paciente__apellido')