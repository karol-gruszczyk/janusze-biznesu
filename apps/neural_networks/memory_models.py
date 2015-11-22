from .models import DatabaseNeuralNetwork, DatabaseNeuron, DatabaseNeuralConnection


class NeuralNetwork:
    input_neurons = []
    output_neurons = []

    def __init__(self):
        pass

    @classmethod
    def read_from_database(cls, neural_network: DatabaseNeuralNetwork) -> NeuralNetwork:
        net = NeuralNetwork()

        def read_net(neuron: DatabaseNeuron):
            
        for input_neuron in neural_network.input_neurons:
            neuron = Neuron()

            net.input_neurons.append(neuron)

    def save_to_database(self):
        pass


class Neuron:
    forward_connections = []
    backward_connection = []


class NeuralConnection:
    previous_neuron = None
    next_neuron = None
    weight = float()

    def __init__(self, previous_neuron: Neuron, next_neuron: Neuron, weight: float) -> None:
        self.previous_neuron = previous_neuron
        self.next_neuron = next_neuron
        self.weight = weight
