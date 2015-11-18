# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0014_auto_20151113_0916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('lower_record', models.OneToOneField(related_name='upper_gain', to='shares.ShareRecord')),
                ('share', models.ForeignKey(to='shares.Share')),
                ('upper_record', models.OneToOneField(related_name='lower_gain', to='shares.ShareRecord')),
            ],
        ),
    ]
