from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import FormularioCreacionUsuario, FormularioAutenticacion
from .models import Usuario

def vista_login(request):
    if request.method == 'POST':
        formulario = FormularioAutenticacion(data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
            if usuario.rol == 'jefe':
                return redirect('informes:estadisticas')
            elif usuario.rol == 'admin':
                return redirect('cuentas:gestion_usuarios')
            else:
                return redirect('pacientes:lista_pacientes')
    else:
        formulario = FormularioAutenticacion()
    return render(request, 'cuentas/login.html', {'formulario': formulario})

@login_required
def vista_logout(request):
    logout(request)
    return redirect('cuentas:login')

@login_required
def gestion_usuarios(request):
    if request.user.rol != 'admin':
        return redirect('pacientes:lista_pacientes')
    
    if request.method == 'POST':
        formulario = FormularioCreacionUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('cuentas:gestion_usuarios')
    else:
        formulario = FormularioCreacionUsuario()
    
    usuarios = Usuario.objects.all()
    return render(request, 'cuentas/gestion_usuarios.html', {'formulario': formulario, 'usuarios': usuarios})