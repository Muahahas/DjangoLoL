# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0037_auto_20150516_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 17, 14, 59, 40, 847223)),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='reclamacio',
            unique_together=set([('jugador', 'partida')]),
        ),
    ]
