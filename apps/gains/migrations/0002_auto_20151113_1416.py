# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gains', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gain',
            name='amount',
        ),
        migrations.AddField(
            model_name='gain',
            name='close_gain',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gain',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 11, 13, 13, 16, 8, 160509, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gain',
            name='high_gain',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gain',
            name='low_gain',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gain',
            name='open_gain',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gain',
            name='volume_gain',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
