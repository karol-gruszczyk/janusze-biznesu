# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0012_share_last_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='share',
            options={'get_latest_by': 'last_updated'},
        ),
    ]
