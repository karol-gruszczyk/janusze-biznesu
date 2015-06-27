# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0007_share_visible_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='share',
            name='first_record',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='share',
            name='last_record',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='share',
            name='records',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
