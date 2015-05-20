# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0057_auto_20150520_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 20, 20, 33, 33, 880583)),
            preserve_default=True,
        ),
    ]
