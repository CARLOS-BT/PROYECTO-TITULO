from django import forms

class FormularioFiltroEstadisticas(forms.Form):
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    fecha_fin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    estado = forms.ChoiceField(choices=[('all', 'Todos'), ('en_proceso', 'En Proceso'), ('terminado', 'Terminado'), ('no_terminado', 'No Terminado')], required=False)