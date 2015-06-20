# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0003_sharegroup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharegroup',
            name='relation',
        ),
        migrations.AddField(
            model_name='sharegroup',
            name='shares',
            field=models.ManyToManyField(to='shares.Share'),
        ),
    ]
