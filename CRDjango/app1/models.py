from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField('Nombre', max_length=40)
    gender = models.BooleanField('Sexo')
    power = models.IntegerField('Poder')
    lives = models.IntegerField('Vidas')
    gems = models.IntegerField('Gemas')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Jugadores'
        verbose_name_plural = 'Jugadores'
