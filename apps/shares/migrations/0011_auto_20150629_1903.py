# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0010_auto_20150628_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='share',
            name='visible_name',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sharerecord',
            name='date',
            field=models.DateField(db_index=True),
        ),
    ]
