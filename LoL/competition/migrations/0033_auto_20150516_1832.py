# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0032_auto_20150516_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamacio',
            name='jugador',
            field=models.ForeignKey(default=1, to='competition.Jugador'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 16, 18, 32, 15, 33385)),
            preserve_default=True,
        ),
    ]
