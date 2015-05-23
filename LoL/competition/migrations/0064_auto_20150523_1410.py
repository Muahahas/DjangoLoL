# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0063_auto_20150522_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titol', models.CharField(max_length=50)),
                ('cosNoticia', models.CharField(max_length=400)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 5, 23, 14, 10, 50, 565913))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 23, 14, 10, 50, 559469)),
            preserve_default=True,
        ),
    ]
