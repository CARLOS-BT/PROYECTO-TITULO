from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Sesion
from .forms import FormularioPaciente, FormularioSesion

@login_required
def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/lista_pacientes.html', {'pacientes': pacientes})

@login_required
def detalle_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    sesiones = paciente.sesiones.all()
    return render(request, 'pacientes/detalle_paciente.html', {'paciente': paciente, 'sesiones': sesiones})

@login_required
def crear_paciente(request):
    if request.method == 'POST':
        formulario = FormularioPaciente(request.POST)
        if formulario.is_valid():
            paciente = formulario.save(commit=False)
            paciente.kinesiologo = request.user
            paciente.save()
            return redirect('pacientes:detalle_paciente', pk=paciente.pk)
    else:
        formulario = FormularioPaciente()
    return render(request, 'pacientes/formulario_paciente.html', {'formulario': formulario})

@login_required
def actualizar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        formulario = FormularioPaciente(request.POST, instance=paciente)
        if formulario.is_valid():
            formulario.save()
            return redirect('pacientes:detalle_paciente', pk=paciente.pk)
    else:
        formulario = FormularioPaciente(instance=paciente)
    return render(request, 'pacientes/formulario_paciente.html', {'formulario': formulario})

@login_required
def crear_sesion(request, paciente_pk):
    paciente = get_object_or_404(Paciente, pk=paciente_pk)
    if request.method == 'POST':
        formulario = FormularioSesion(request.POST)
        if formulario.is_valid():
            sesion = formulario.save(commit=False)
            sesion.paciente = paciente
            sesion.save()
            return redirect('pacientes:detalle_paciente', pk=paciente.pk)
    else:
        formulario = FormularioSesion()
    return render(request, 'pacientes/formulario_sesion.html', {'formulario': formulario, 'paciente': paciente})