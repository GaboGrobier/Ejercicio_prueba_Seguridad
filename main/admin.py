from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'username')  # Campos que se mostrarán en la lista
    search_fields = ('nombre', 'email', 'username')  # Campos que se pueden buscar
    list_filter = ('email',)  # Campos que se pueden filtrar
