# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0031_auto_20150516_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reclamacio',
            name='jornada',
        ),
        migrations.RemoveField(
            model_name='reclamacio',
            name='jugador',
        ),
        migrations.RemoveField(
            model_name='reclamacio',
            name='lliga',
        ),
        migrations.RemoveField(
            model_name='reclamacio',
            name='partida',
        ),
        migrations.AddField(
            model_name='reclamacio',
            name='team',
            field=models.ForeignKey(default=1, to='competition.Equip'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 16, 18, 19, 32, 298784)),
            preserve_default=True,
        ),
    ]
