from django.contrib import admin
from .models import Articulo, Usuario

# Register your models here.

class ArticuloAdm(admin.ModelAdmin):
	list_display = ('Titulo', 'Contenido', 'FK_Usuario')
	search_fields = ('Titulo', 'Contenido', 'FK_Usuario')
	
	
admin.site.register(Articulo, ArticuloAdm)

class UsuarioAdm(admin.ModelAdmin):
	list_display = ('Nombre')
	search_fields = ('Nombre')
	
	
admin.site.register(Usuario, UsuarioAdm)