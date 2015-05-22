# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0060_auto_20150521_1852'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EquipXML',
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 22, 14, 55, 10, 655276)),
            preserve_default=True,
        ),
    ]
