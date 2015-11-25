# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neural_networks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='databaseneuralnetwork',
            name='input_neurons',
            field=models.ForeignKey(to='neural_networks.DatabaseNeuron', related_name='+'),
        ),
        migrations.AlterField(
            model_name='databaseneuralnetwork',
            name='output_neurons',
            field=models.ForeignKey(to='neural_networks.DatabaseNeuron', related_name='+'),
        ),
    ]
