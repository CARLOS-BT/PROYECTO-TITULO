from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    RUT = models.CharField(max_length=12, unique=True)
    ROLES = (
        ('kinesiologo', 'Kinesiólogo'),
        ('asistente', 'Asistente'),
        ('jefe', 'Jefe de Clínica'),
        ('admin', 'Administrador'),
    )
    rol = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return f"{self.username} - {self.get_rol_display()}"