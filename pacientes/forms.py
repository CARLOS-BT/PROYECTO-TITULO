from django import forms
from .models import Paciente, Sesion

class FormularioPaciente(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'rut', 'patologia', 'observaciones', 'fecha_inicio', 'fecha_termino', 'estado']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_termino': forms.DateInput(attrs={'type': 'date'}),
        }

class FormularioSesion(forms.ModelForm):
    class Meta:
        model = Sesion
        fields = ['fecha', 'completada', 'notas']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }