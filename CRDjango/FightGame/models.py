from django.db import models

# Create your models here.

CATEGORIES = (
    (0, 'Pluma'),
    (1, 'Medio'),
    (2, 'Pesado')
)

class Bicho(models.Model):
    alias = models.CharField('Mote', max_length=20)
    skills = models.IntegerField(default=0)
    force = models.IntegerField(default=0)
    resistance = models.IntegerField(default=0)

    def __str__(self):
        return self.alias

    class Meta:
        verbose_name = 'Luchador'
        verbose_name_plural = 'Luchadores'

class Tournament(models.Model):
    name = models.CharField('Nombre', max_length=25)
    start_date = models.DateTimeField('Fecha/Hora de inicio')
    end = models.DateTimeField('Fecha/Hora final')
    category = models.IntegerField('Categoría', default=0, choices=CATEGORIES)
    fighters = models.ManyToManyField(Bicho, verbose_name='Luchadores')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Torneo'

class Combat(models.Model):
    tournament = models.ForeignKey(Tournament, verbose_name='Torneo', on_delete=models.CASCADE)
    date = models.DateTimeField('Fecha/Hora de inicio')
    fighter1 = models.ForeignKey(Bicho, verbose_name='Luchador 1', related_name='cf1', on_delete=models.CASCADE)
    fighter2 = models.ForeignKey(Bicho, verbose_name='Luchador 2', related_name='cf2', on_delete=models.CASCADE)
    winner = models.ForeignKey(Bicho, verbose_name='Ganador', related_name='combat_winner', on_delete=models.CASCADE)

    def __str__(self):
        return '{} vs {}'.format(self.fighter1.alias, self.fighter2.alias)

    class Meta:
        verbose_name = 'Combate'