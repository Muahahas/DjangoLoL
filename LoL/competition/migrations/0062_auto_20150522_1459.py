# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0061_auto_20150522_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamacio',
            name='response',
            field=models.CharField(max_length=300, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reclamacio',
            name='solved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 22, 14, 59, 28, 367909)),
            preserve_default=True,
        ),
    ]
