# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gains', '0003_auto_20151118_0918'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gain',
            options={'ordering': ['lower_record']},
        ),
        migrations.AlterField(
            model_name='gain',
            name='share',
            field=models.ForeignKey(related_name='gains', to='shares.Share'),
        ),
    ]
