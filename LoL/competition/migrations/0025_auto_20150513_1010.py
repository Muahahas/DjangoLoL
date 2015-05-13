# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0024_auto_20150513_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='jornada',
            name='league',
            field=models.ForeignKey(default=1, to='competition.Lliga'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partida',
            name='jornada',
            field=models.ForeignKey(default=1, to='competition.Jornada'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 13, 10, 9, 40, 670718, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
