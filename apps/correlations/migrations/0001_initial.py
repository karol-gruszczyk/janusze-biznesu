# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0014_auto_20151113_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Correlation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('day_interval', models.PositiveSmallIntegerField()),
                ('value', models.FloatField()),
                ('input_shares', models.ForeignKey(related_name='+', to='shares.Share')),
                ('output_shares', models.ForeignKey(related_name='+', to='shares.Share')),
            ],
        ),
    ]
