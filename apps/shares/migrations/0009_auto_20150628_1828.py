# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0008_auto_20150627_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharegroup',
            name='verbose_name',
            field=models.CharField(null=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='share',
            name='name',
            field=models.CharField(max_length=32, db_index=True),
        ),
        migrations.AlterField(
            model_name='sharegroup',
            name='name',
            field=models.CharField(max_length=32, db_index=True),
        ),
    ]
