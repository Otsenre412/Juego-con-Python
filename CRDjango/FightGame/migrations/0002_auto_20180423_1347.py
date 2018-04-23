# Generated by Django 2.0.4 on 2018-04-23 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FightGame', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bicho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=20, verbose_name='Mote')),
                ('skills', models.IntegerField(default=0)),
                ('force', models.IntegerField(default=0)),
                ('resistance', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Luchador',
                'verbose_name_plural': 'Luchadores',
            },
        ),
        migrations.CreateModel(
            name='Combat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Fecha/Hora de inicio')),
                ('fighter1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cf1', to='FightGame.Bicho', verbose_name='Luchador 1')),
                ('fighter2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cf2', to='FightGame.Bicho', verbose_name='Luchador 2')),
            ],
            options={
                'verbose_name': 'Combate',
                'verbose_name_plural': 'Combates',
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Nombre')),
                ('start_date', models.DateTimeField(verbose_name='Fecha/Hora de inicio')),
                ('end', models.DateTimeField(verbose_name='Fecha/Hora final')),
                ('category', models.IntegerField(choices=[(0, 'Pluma'), (1, 'Medio'), (2, 'Pesado')], default=0, verbose_name='Categoría')),
                ('fighters', models.ManyToManyField(to='FightGame.Bicho', verbose_name='Luchadores')),
            ],
            options={
                'verbose_name': 'Torneo',
            },
        ),
        migrations.DeleteModel(
            name='Bichos',
        ),
        migrations.AddField(
            model_name='combat',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FightGame.Tournament', verbose_name='Torneo'),
        ),
    ]