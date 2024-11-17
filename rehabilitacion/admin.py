from django.contrib import admin
from .models import PlanRehabilitacion

@admin.register(PlanRehabilitacion)
class PlanRehabilitacionAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'sesiones_totales', 'sesiones_completadas', 'fecha_inicio', 'fecha_termino')
    list_filter = ('fecha_inicio', 'fecha_termino')
    search_fields = ('paciente__nombre', 'paciente__apellido')