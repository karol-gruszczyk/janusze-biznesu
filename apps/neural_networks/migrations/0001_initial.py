# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatabaseNeuralConnection',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DatabaseNeuralNetwork',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='DatabaseNeuron',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
            ],
        ),
        migrations.AddField(
            model_name='databaseneuralnetwork',
            name='input_neurons',
            field=models.ForeignKey(related_name='input_neurons', to='neural_networks.DatabaseNeuron'),
        ),
        migrations.AddField(
            model_name='databaseneuralnetwork',
            name='output_neurons',
            field=models.ForeignKey(related_name='output_neurons', to='neural_networks.DatabaseNeuron'),
        ),
        migrations.AddField(
            model_name='databaseneuralconnection',
            name='next_neuron',
            field=models.ForeignKey(related_name='backward_connections', to='neural_networks.DatabaseNeuron'),
        ),
        migrations.AddField(
            model_name='databaseneuralconnection',
            name='previous_neuron',
            field=models.ForeignKey(related_name='forward_connections', to='neural_networks.DatabaseNeuron'),
        ),
    ]
