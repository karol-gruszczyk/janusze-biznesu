# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0009_auto_20150628_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='share',
            name='name',
            field=models.CharField(max_length=32, db_index=True, unique=True),
        ),
        migrations.AlterField(
            model_name='sharegroup',
            name='name',
            field=models.CharField(max_length=32, db_index=True, unique=True),
        ),
    ]
