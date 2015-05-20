# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0056_auto_20150520_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jornada',
            old_name='read',
            new_name='isReady',
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 20, 20, 19, 45, 678558)),
            preserve_default=True,
        ),
    ]
