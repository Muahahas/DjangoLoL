# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0021_auto_20150511_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equip',
            name='correoe',
            field=models.EmailField(unique=True, max_length=75, verbose_name=b'email'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 11, 14, 39, 6, 550236, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
