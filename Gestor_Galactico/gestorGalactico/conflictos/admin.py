from django.contrib import admin

from.models import Conflicto, Datos

class ConflictoAdm(admin.ModelAdmin):
    list_display = ('sistema', 'tipo', 'seguridad', 'miBando')
    search_fields = ('sistema', 'tipo', 'seguridad', 'miBando')

class DatosAdm(admin.ModelAdmin):
    list_display = ('bandoEnemigo', 'fechahora', 'estado', 'estadoAvance')

admin.site.register(Conflicto, ConflictoAdm)
admin.site.register(Datos, DatosAdm)