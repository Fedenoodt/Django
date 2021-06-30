from django.db import models

# Create your models here.
from django.utils import timezone

class Conflicto(models.Model):
    sistema = models.CharField(max_length=400, default="")
    tipo = models.CharField(max_length=400, default="")
    seguridad = models.CharField(max_length=400, default="")
    miBando = models.CharField(max_length=400, default="")

    class Meta:
        ordering = ('sistema',)

    def __str__(self):
        return self.sistema

class Datos(models.Model):
    ESTADOS = (
        ('Pendiente', 'Pendiente'),
        ('Derrota', 'Derrota'),
        ('Retirada', 'Retirada'),
        ('Victoria', 'Victoria')
    )

    bandoEnemigo = models.ForeignKey('bandoEnemigo', on_delete=models.CASCADE)
    fechahora = models.DateTimeField(default=timezone.now)
    estado = models.CharField(max_length=8,
                              choices=ESTADOS,
                              default='Pendiente')
    estadoAvance = models.CharField(max_length=400, default="")

    class Meta:
        ordering = ('-fechahora',)

    def __str__(self):
        return str(self.fechahora) + '-' + str(self.bandoEnemigo)