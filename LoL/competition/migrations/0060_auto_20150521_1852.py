# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0059_auto_20150521_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipxml',
            name='email',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipxml',
            name='isTeamValid',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 21, 18, 52, 6, 14518)),
            preserve_default=True,
        ),
    ]
