# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0023_auto_20150511_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='email',
            field=models.EmailField(default=1, max_length=75),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 13, 8, 11, 48, 727832, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
