# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0002_auto_20150506_0753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estadistiques',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mortsEquip', models.IntegerField(default=0)),
                ('killsEquip', models.IntegerField(default=0)),
                ('assistEquip', models.IntegerField(default=0)),
                ('team', models.ForeignKey(to='competition.Equip')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 5, 6, 11, 50, 12, 890702, tzinfo=utc))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lliga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codi', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codi', models.IntegerField(default=0)),
                ('ip', models.CharField(max_length=15)),
                ('equipA', models.ManyToManyField(to='competition.Equip')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resultat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mortsEquipA', models.IntegerField(default=0)),
                ('killsEquipA', models.IntegerField(default=0)),
                ('assistEquipA', models.IntegerField(default=0)),
                ('mortsEquipB', models.IntegerField(default=0)),
                ('killsEquipB', models.IntegerField(default=0)),
                ('assistEquipB', models.IntegerField(default=0)),
                ('partida', models.OneToOneField(to='competition.Partida')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='jugador',
            name='lastName',
        ),
    ]
