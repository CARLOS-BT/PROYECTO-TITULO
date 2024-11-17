from django import forms
from .models import PlanRehabilitacion

class FormularioPlanRehabilitacion(forms.ModelForm):
    class Meta:
        model = PlanRehabilitacion
        fields = ['sesiones_totales', 'fecha_inicio', 'fecha_termino']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_termino': forms.DateInput(attrs={'type': 'date'}),
        }