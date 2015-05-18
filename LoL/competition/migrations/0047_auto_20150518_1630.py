# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0046_auto_20150518_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.IntegerField(default=0)),
                ('equip', models.ForeignKey(to='competition.Equip')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='classificacio',
            name='equips',
            field=models.ForeignKey(default=1, to='competition.Equip'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 18, 16, 30, 17, 171739)),
            preserve_default=True,
        ),
    ]
