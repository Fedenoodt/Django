import usuario
from django.contrib import admin

# Register your models here.

admin.site.register(usuario.models.Usuario)
admin.site.register(usuario.models.Articulo)