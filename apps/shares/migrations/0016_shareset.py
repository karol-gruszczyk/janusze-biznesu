# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0015_auto_20151125_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareSet',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('shares', models.ManyToManyField(to='shares.Share')),
            ],
        ),
    ]
