from django.db import models


class DatabaseNeuron(models.Model):
    pass


class DatabaseNeuralConnection(models.Model):
    previous_neuron = models.ForeignKey(DatabaseNeuron, related_name='forward_connections')
    next_neuron = models.ForeignKey(DatabaseNeuron, related_name='backward_connections')
    weight = models.FloatField()


class DatabaseNeuralNetwork(models.Model):
    input_neurons = models.ForeignKey(DatabaseNeuron, related_name='+')
    output_neurons = models.ForeignKey(DatabaseNeuron, related_name='+')

