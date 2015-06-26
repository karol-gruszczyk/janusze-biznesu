# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0005_auto_20150626_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='share',
            name='updated_daily',
            field=models.BooleanField(default=False),
        ),
    ]
