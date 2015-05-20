# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0053_auto_20150520_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='jornada',
            name='read',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 20, 19, 44, 13, 239541)),
            preserve_default=True,
        ),
    ]
