# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competition', '0003_auto_20150506_1150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equip',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveField(
            model_name='equip',
            name='id',
        ),
        migrations.RemoveField(
            model_name='equip',
            name='password',
        ),
        migrations.AddField(
            model_name='equip',
            name='user_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=1, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='equip',
            name='name',
            field=models.CharField(unique=True, max_length=25),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 6, 21, 13, 9, 939785, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='jugador',
            name='correu',
            field=models.EmailField(max_length=50),
            preserve_default=True,
        ),
    ]
