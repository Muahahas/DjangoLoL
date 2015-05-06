# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('rol', models.CharField(max_length=3, choices=[(b'Top', b'Top'), (b'ADC', b'AD Carry'), (b'Sup', b'Support'), (b'Jung', b'Jungle'), (b'Mid', b'Middle')])),
                ('correu', models.CharField(max_length=50)),
                ('top', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
