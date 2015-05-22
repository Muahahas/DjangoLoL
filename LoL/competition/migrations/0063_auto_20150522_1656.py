# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0062_auto_20150522_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 22, 16, 56, 21, 679160)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='reclamacio',
            name='response',
            field=models.CharField(default=1, max_length=300, blank=True),
            preserve_default=False,
        ),
    ]
