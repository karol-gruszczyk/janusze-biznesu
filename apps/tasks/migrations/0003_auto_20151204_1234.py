# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20150701_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('datetime_added', models.DateTimeField(auto_now_add=True)),
                ('execution_date', models.TimeField(blank=True)),
                ('progress', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
