# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0064_auto_20150523_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='lliga',
            name='finished',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 2, 18, 24, 8, 456297)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 2, 18, 24, 8, 463759)),
            preserve_default=True,
        ),
    ]
