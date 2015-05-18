# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0040_auto_20150518_0940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classificacio',
            name='jornada',
        ),
        migrations.AddField(
            model_name='classificacio',
            name='league',
            field=models.OneToOneField(default=1, to='competition.Lliga'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resultat',
            name='winner',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 18, 11, 7, 31, 255980)),
            preserve_default=True,
        ),
    ]
