# Generated by Django 2.0.4 on 2018-04-23 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FightGame', '0003_auto_20180423_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combat',
            name='winner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='combat_winner', to='FightGame.Bicho', verbose_name='Ganador'),
            preserve_default=False,
        ),
    ]