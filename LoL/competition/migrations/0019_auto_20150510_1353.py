# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0018_auto_20150509_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 10, 13, 53, 7, 255249, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jugador',
            name='rol',
            field=models.CharField(max_length=3, choices=[(b'Top', b'Top'), (b'ADC', b'AD Carry'), (b'Sup', b'Support'), (b'Jun', b'Jungle'), (b'Mid', b'Middle')]),
            preserve_default=True,
        ),
    ]
