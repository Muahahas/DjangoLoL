# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0047_auto_20150518_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classificacio',
            name='equips',
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 18, 16, 36, 26, 520085)),
            preserve_default=True,
        ),
    ]
