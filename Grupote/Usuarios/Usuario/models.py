from django.db import models
from django.db.models.base import ModelBase

# Create your models here.

class Usuario(models.Model):
    usuarioID = models.CharField(primary_key = True)
    nombre = models.CharField(max_length = 50)

class Articulo(models.Model):
    articuloID = models.CharField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length = 300)