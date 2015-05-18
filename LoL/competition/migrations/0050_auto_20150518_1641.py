# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0049_auto_20150518_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipposition',
            name='clas',
            field=models.ForeignKey(default=1, to='competition.Classificacio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 18, 16, 41, 30, 378151)),
            preserve_default=True,
        ),
    ]
