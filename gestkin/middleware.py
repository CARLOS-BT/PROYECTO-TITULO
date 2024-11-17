from django.shortcuts import redirect
from django.urls import reverse

class RoleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if request.path.startswith('/admin/') and request.user.rol != 'admin':
                return redirect('pacientes:lista_pacientes')
            if request.path.startswith('/informes/') and request.user.rol != 'jefe':
                return redirect('pacientes:lista_pacientes')
        return self.get_response(request)