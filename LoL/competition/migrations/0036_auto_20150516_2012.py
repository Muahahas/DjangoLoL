# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0035_auto_20150516_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamacio',
            name='jornada',
            field=models.ForeignKey(default=1, to='competition.Jornada'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 16, 20, 12, 27, 605245)),
            preserve_default=True,
        ),
    ]
