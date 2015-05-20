# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0055_auto_20150520_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='equip',
            name='isReady',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 20, 20, 5, 37, 92045)),
            preserve_default=True,
        ),
    ]
