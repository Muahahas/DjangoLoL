# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0019_auto_20150510_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='equip',
            name='correoe',
            field=models.EmailField(default=1, unique=True, max_length=75),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 11, 14, 6, 40, 206523, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
