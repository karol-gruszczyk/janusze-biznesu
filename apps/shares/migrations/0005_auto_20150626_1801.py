# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0004_auto_20150620_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharegroup',
            name='shares',
            field=models.ManyToManyField(blank=True, to='shares.Share'),
        ),
    ]
