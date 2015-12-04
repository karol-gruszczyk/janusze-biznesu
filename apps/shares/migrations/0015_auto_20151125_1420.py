# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0014_auto_20151113_0916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='share',
            old_name='records',
            new_name='num_records',
        ),
        migrations.AlterField(
            model_name='sharerecord',
            name='share',
            field=models.ForeignKey(related_name='records', to='shares.Share'),
        ),
    ]
