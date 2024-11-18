from django.urls import path
from . import views

app_name = 'informes'

urlpatterns = [
    path('estadisticas/', views.estadisticas, name='estadisticas'),
]
