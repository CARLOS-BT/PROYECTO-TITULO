from django.urls import path
from . import views

app_name = 'cuentas'

urlpatterns = [
    path('', views.vista_login, name='login'),
    path('logout/', views.vista_logout, name='logout'),
    path('gestion-usuarios/', views.gestion_usuarios, name='gestion_usuarios'),
]