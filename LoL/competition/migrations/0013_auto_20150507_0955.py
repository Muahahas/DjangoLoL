# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0012_auto_20150506_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jugador',
            name='correu',
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 7, 9, 55, 38, 973304, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jugador',
            name='team',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
