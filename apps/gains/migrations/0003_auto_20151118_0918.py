# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gains', '0002_auto_20151113_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gain',
            name='date',
            field=models.DateField(db_index=True),
        ),
        migrations.AlterIndexTogether(
            name='gain',
            index_together=set([('share', 'date')]),
        ),
    ]
