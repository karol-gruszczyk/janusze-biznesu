# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0016_shareset'),
        ('correlations', '0002_auto_20151126_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorrelationSet',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('day_interval_start', models.SmallIntegerField()),
                ('day_interval_end', models.SmallIntegerField()),
                ('from_date', models.DateField()),
                ('shares', models.ManyToManyField(related_name='+', to='shares.Share')),
            ],
        ),
    ]
