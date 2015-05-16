# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0034_auto_20150516_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamacio',
            name='partida',
            field=models.ForeignKey(default=1, to='competition.Partida'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 16, 19, 49, 0, 616118)),
            preserve_default=True,
        ),
    ]
