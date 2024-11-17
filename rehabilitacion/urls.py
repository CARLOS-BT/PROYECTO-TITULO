from django.urls import path
from . import views

app_name = 'rehabilitacion'

urlpatterns = [
    path('crear/<int:paciente_id>/', views.crear_plan_rehabilitacion, name='crear_plan'),
    path('actualizar/<int:plan_id>/', views.actualizar_plan_rehabilitacion, name='actualizar_plan'),
]