# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0036_auto_20150516_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamacio',
            name='lliga',
            field=models.ForeignKey(default=1, to='competition.Lliga'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 16, 20, 20, 21, 398951)),
            preserve_default=True,
        ),
    ]
