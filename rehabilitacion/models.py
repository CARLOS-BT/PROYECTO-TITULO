from django.db import models
from pacientes.models import Paciente

class PlanRehabilitacion(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE, related_name='plan_rehabilitacion')
    sesiones_totales = models.IntegerField()
    sesiones_completadas = models.IntegerField(default=0)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()

    def __str__(self):
        return f"Plan de {self.paciente} - {self.sesiones_completadas}/{self.sesiones_totales} sesiones"