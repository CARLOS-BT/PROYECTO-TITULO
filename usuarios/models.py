from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=10, unique=True)
    rol = models.CharField(
        max_length=20,
        choices=[('admin', 'Administrador'), ('jefe', 'Jefe de Clínica'), ('kinesiologo', 'Kinesiólogo'), ('asistente', 'Asistente')],
        default='asistente'
    )

    def __str__(self):
        return f"{self.nombre} ({self.rut}) - {self.rol}"
