# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0002_sharerecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('relation', models.ManyToManyField(null=True, to='shares.Share')),
            ],
        ),
    ]
