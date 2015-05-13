# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0022_auto_20150511_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='equip',
            name='isTeamValid',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 11, 22, 41, 54, 868399, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
