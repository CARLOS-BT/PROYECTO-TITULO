from django.db import models
from cuentas.models import Usuario

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    patologia = models.CharField(max_length=200)
    observaciones = models.TextField(blank=True)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    ESTADOS = [
        ('en_proceso', 'En Proceso'),
        ('terminado', 'Terminado'),
        ('no_terminado', 'No Terminado'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS)
    kinesiologo = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='pacientes')

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.rut}"

class Sesion(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='sesiones')
    fecha = models.DateField()
    completada = models.BooleanField(default=False)
    notas = models.TextField(blank=True)

    def __str__(self):
        return f"Sesión de {self.paciente} - {self.fecha}"
    