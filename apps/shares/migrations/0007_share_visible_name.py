# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0006_auto_20150626_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='share',
            name='visible_name',
            field=models.CharField(null=True, max_length=64),
        ),
    ]
