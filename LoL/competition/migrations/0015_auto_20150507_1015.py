# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0014_auto_20150507_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 7, 10, 15, 30, 732373, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
