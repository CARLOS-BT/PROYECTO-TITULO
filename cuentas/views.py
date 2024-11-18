from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import FormularioCreacionUsuario, FormularioAutenticacion
from .models import Usuario
from django.http import HttpResponseForbidden


# Decorador para verificar si un usuario es administrador
def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser and request.user.rol != 'admin':
            return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
        return view_func(request, *args, **kwargs)
    return wrapper


# Vista para iniciar sesión
def vista_login(request):
    if request.method == 'POST':
        formulario = FormularioAutenticacion(data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)

            # Redirección según el tipo de usuario
            if usuario.is_superuser:
                return redirect('/admin/')  # Redirige al panel de administración
            elif usuario.rol == 'admin':
                return redirect('/admin/')  # Redirige al panel de administración
            elif usuario.rol == 'jefe':
                return redirect('informes:estadisticas')  # Redirige a estadísticas
            else:
                return redirect('pacientes:lista_pacientes')  # Redirige a pacientes
    else:
        formulario = FormularioAutenticacion()

    return render(request, 'cuentas/login.html', {'formulario': formulario})


# Vista para cerrar sesión
@login_required
def vista_logout(request):
    logout(request)
    return redirect('cuentas:login')  # Redirige a la página de inicio de sesión


# Vista para la gestión de usuarios (exclusivo para administradores)
@login_required
@admin_required
def gestion_usuarios(request):
    if request.method == 'POST':
        formulario = FormularioCreacionUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('cuentas:gestion_usuarios')
    else:
        formulario = FormularioCreacionUsuario()

    # Listar todos los usuarios
    usuarios = Usuario.objects.all()
    return render(request, 'cuentas/gestion_usuarios.html', {'formulario': formulario, 'usuarios': usuarios})
