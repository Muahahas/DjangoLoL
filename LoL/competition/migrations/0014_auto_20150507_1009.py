# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0013_auto_20150507_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 7, 10, 9, 30, 661790, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jugador',
            name='team',
            field=models.ForeignKey(to='competition.Equip'),
            preserve_default=True,
        ),
    ]
