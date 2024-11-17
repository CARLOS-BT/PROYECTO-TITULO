from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from pacientes.models import Paciente
from django.db.models import Count
from django.utils import timezone
from .forms import FormularioFiltroEstadisticas

@login_required
def estadisticas(request):
    if request.user.rol != 'jefe':
        return redirect('pacientes:lista_pacientes')

    formulario = FormularioFiltroEstadisticas(request.GET)
    pacientes = Paciente.objects.all()
    
    if formulario.is_valid():
        fecha_inicio = formulario.cleaned_data.get('fecha_inicio')
        fecha_fin = formulario.cleaned_data.get('fecha_fin')
        estado = formulario.cleaned_data.get('estado')
        
        if fecha_inicio:
            pacientes = pacientes.filter(fecha_inicio__gte=fecha_inicio)
        if fecha_fin:
            pacientes = pacientes.filter(fecha_termino__lte=fecha_fin)
        if estado and estado != 'all':
            pacientes = pacientes.filter(estado=estado)

    total_pacientes = pacientes.count()
    pacientes_completados = pacientes.filter(estado='terminado').count()
    pacientes_no_completados = pacientes.filter(estado='no_terminado').count()
    pacientes_en_proceso = pacientes.filter(estado='en_proceso').count()

    contexto = {
        'formulario': formulario,
        'total_pacientes': total_pacientes,
        'pacientes_completados': pacientes_completados,
        'pacientes_no_completados': pacientes_no_completados,
        'pacientes_en_proceso': pacientes_en_proceso,
    }

    return render(request, 'informes/estadisticas.html', contexto)