# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0011_auto_20150629_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='share',
            name='last_updated',
            field=models.DateTimeField(null=True),
        ),
    ]
