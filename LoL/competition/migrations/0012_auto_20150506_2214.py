# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0011_auto_20150506_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equip',
            name='name',
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 6, 22, 14, 17, 304497, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
