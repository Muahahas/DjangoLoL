# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0039_auto_20150517_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classificacio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jornada', models.OneToOneField(to='competition.Jornada')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 18, 9, 40, 52, 158019)),
            preserve_default=True,
        ),
    ]
