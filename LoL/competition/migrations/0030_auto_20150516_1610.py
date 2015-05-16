# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0029_auto_20150514_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reclamacio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=300)),
                ('jornada', models.ForeignKey(to='competition.Jornada')),
                ('jugador', models.ForeignKey(to='competition.Jugador')),
                ('lliga', models.ForeignKey(to='competition.Lliga')),
                ('partida', models.ForeignKey(to='competition.Partida')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='jornada',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 10, 31, 224608)),
            preserve_default=True,
        ),
    ]
