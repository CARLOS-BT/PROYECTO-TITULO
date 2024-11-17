from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

class FormularioCreacionUsuario(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'RUT', 'rol', 'password1', 'password2']

class FormularioAutenticacion(AuthenticationForm):
    username = forms.CharField(label='RUT')