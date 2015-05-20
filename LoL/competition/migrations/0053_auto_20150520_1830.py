# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0052_auto_20150518_1844'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipposition',
            options={'ordering': ['points']},
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 20, 18, 30, 51, 493178)),
            preserve_default=True,
        ),
    ]
