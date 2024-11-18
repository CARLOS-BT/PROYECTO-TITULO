from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'RUT', 'rol', 'is_staff')
    list_filter = ('rol', 'is_staff', 'is_superuser')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('RUT', 'rol')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('RUT', 'rol')}),
    )
admin.site.register(Usuario, UsuarioAdmin)