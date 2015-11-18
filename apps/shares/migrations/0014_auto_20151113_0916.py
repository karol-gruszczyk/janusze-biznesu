# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0013_auto_20150701_1254'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sharerecord',
            unique_together=set([('share', 'date')]),
        ),
        migrations.AlterIndexTogether(
            name='sharerecord',
            index_together=set([('share', 'date')]),
        ),
    ]
