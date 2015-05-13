# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0026_auto_20150513_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='jornada',
            name='codi',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 13, 10, 54, 11, 476098, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
