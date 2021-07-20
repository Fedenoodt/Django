from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
    Nombre = models.CharField(max_length=35)

class Articulo(models.Model):
    Titulo = models.CharField(max_length=80)
    Contenido = ''
    FK_Usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)