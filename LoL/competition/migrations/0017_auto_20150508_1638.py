# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0016_auto_20150507_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 8, 16, 38, 50, 596568, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jugador',
            name='name',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jugador',
            name='team',
            field=models.ForeignKey(to='competition.Equip'),
            preserve_default=True,
        ),
    ]
