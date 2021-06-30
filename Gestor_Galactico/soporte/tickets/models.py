from django.db import models

# Create your models here.
from django.utils import timezone


class Cliente(models.Model):
	nombre = models.CharField(max_length=120, default="")
	dni = models.CharField(max_length=8, default="")
	telefono = models.CharField(max_length=30)
	mail = models.CharField(max_length=100)
	
	class Meta:
		ordering = ('nombre',)
	
	def __str__(self):
		return self.nombre
		
class Ticket(models.Model):
	ESTADOS = (
		('P', 'Pendiente'),
		('C', 'Cerrado'),
		('E', 'En curso'),
	)
	
	cliente_fk = models.ForeignKey('cliente', on_delete=models.CASCADE)
	fechahora = models.DateTimeField(default=timezone.now)
	estado = models.CharField(max_length=8,
		choices=ESTADOS,
		default='P')
	descripcion = models.CharField(max_length=250, default="")
	
	class Meta:
		ordering = ('-fechahora',)
	
	def __str__(self):
		return str(self.fechahora) + '-' + str(self.cliente_fk)
