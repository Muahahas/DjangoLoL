# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0044_auto_20150518_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='lliga',
            name='equips',
            field=models.ManyToManyField(to='competition.Equip'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 18, 12, 16, 43, 639256)),
            preserve_default=True,
        ),
    ]
