from django.db import models


class DatabaseNeuralNetwork(models.Model):
    input_neurons = models.ForeignKey(DatabaseNeuron)
    output_neurons = models.ForeignKey(DatabaseNeuron)


class DatabaseNeuron(models.Model):
    neural_network = models.ForeignKey(DatabaseNeuralNetwork)

    @property
    def backward_connections(self):
        return DatabaseNeuralConnection.objects.filter(next_neuron=self)

    @property
    def forward_connections(self):
        return DatabaseNeuralConnection.objects.filter(previous_neuron=self)


class DatabaseNeuralConnection(models.Model):
    neural_network = models.ForeignKey(DatabaseNeuralNetwork)
    previous_neuron = models.ForeignKey(DatabaseNeuron)
    next_neuron = models.ForeignKey(DatabaseNeuron)
    weight = models.FloatField()
