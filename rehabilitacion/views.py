from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import PlanRehabilitacion
from pacientes.models import Paciente
from .forms import FormularioPlanRehabilitacion

@login_required
def crear_plan_rehabilitacion(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        formulario = FormularioPlanRehabilitacion(request.POST)
        if formulario.is_valid():
            plan = formulario.save(commit=False)
            plan.paciente = paciente
            plan.save()
            return redirect('pacientes:detalle_paciente', pk=paciente.id)
    else:
        formulario = FormularioPlanRehabilitacion()
    return render(request, 'rehabilitacion/crear_plan.html', {'formulario': formulario, 'paciente': paciente})

@login_required
def actualizar_plan_rehabilitacion(request, plan_id):
    plan = get_object_or_404(PlanRehabilitacion, id=plan_id)
    if request.method == 'POST':
        formulario = FormularioPlanRehabilitacion(request.POST, instance=plan)
        if formulario.is_valid():
            formulario.save()
            return redirect('pacientes:detalle_paciente', pk=plan.paciente.id)
    else:
        formulario = FormularioPlanRehabilitacion(instance=plan)
    return render(request, 'rehabilitacion/actualizar_plan.html', {'formulario': formulario, 'plan': plan})