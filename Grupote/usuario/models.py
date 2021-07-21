from django.db import models
from django.db.models.fields import AutoField, CharField, TextField

# Create your models here.

class Usuario(models.Model):
    usuarioID = models.AutoField(primary_key = True, null = False, blank = False)
    nombre = CharField(max_length = 50)

class Articulo(models.Model):
    articuloID = models.AutoField(primary_key = True, null = False, blank = False)
    titulo = CharField(max_length = 100)
    autor = CharField(max_length = 50)
    descripcion = CharField(max_length = 200)
    contenido = TextField()