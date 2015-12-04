# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('correlations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='correlation',
            old_name='output_shares',
            new_name='output_share',
        ),
    ]
