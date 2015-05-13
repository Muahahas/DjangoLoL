# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0025_auto_20150513_1010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partida',
            old_name='equipA',
            new_name='equips',
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 13, 10, 19, 5, 645716, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
