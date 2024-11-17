from django.urls import path
from . import views

app_name = 'pacientes'

urlpatterns = [
    path('', views.lista_pacientes, name='lista_pacientes'),
    path('<int:pk>/', views.detalle_paciente, name='detalle_paciente'),
    path('crear/', views.crear_paciente, name='crear_paciente'),
    path('<int:pk>/actualizar/', views.actualizar_paciente, name='actualizar_paciente'),
    path('<int:paciente_pk>/sesion/crear/', views.crear_sesion, name='crear_sesion'),
]