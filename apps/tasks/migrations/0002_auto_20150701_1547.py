# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='datetime_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 1, 13, 47, 20, 849967, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='periodic',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='execution_date',
            field=models.TimeField(blank=True),
        ),
    ]
