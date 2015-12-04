from .models import DatabaseNeuralNetwork, DatabaseNeuron, DatabaseNeuralConnection


class NeuralNetwork:
    input_neurons = []
    output_neurons = []

    def __init__(self, net_id=None):
        self.net_id = net_id

    def read_from_database(self, neural_network: DatabaseNeuralNetwork):
        created_neurons = {}

        def read_net(db_neuron: DatabaseNeuron):
            current_mem_neuron = created_neurons[db_neuron.id]
            for connection in db_neuron.forward_connections:
                next_db_neuron = connection.next_neuron
                if next_db_neuron.id not in created_neurons:
                    new_neuron = Neuron(next_db_neuron.id)
                    created_neurons[new_neuron.neuron_id] = new_neuron
                    read_net(next_db_neuron)
                next_mem_neuron = created_neurons[next_db_neuron.id]
                new_connection = NeuralConnection(current_mem_neuron, next_mem_neuron, connection.weight)
                current_mem_neuron.forward_connections.append(new_connection)
                next_mem_neuron.backward_connection.append(new_connection)

        for input_neuron in neural_network.input_neurons:
            new_input_neuron = Neuron(input_neuron.id)
            self.input_neurons.append(new_input_neuron)
            created_neurons[new_input_neuron.neuron_id] = new_input_neuron
            read_net(input_neuron)

    def save_to_database(self):
        net = DatabaseNeuralNetwork()
        for input_neuron in self.input_neurons:
            pass


class Neuron:
    forward_connections = []
    backward_connection = []

    def __init__(self, neuron_id):
        self.neuron_id = neuron_id

    def __cmp__(self, other):
        return self.neuron_id == other.neuron_id


class NeuralConnection:
    previous_neuron = None
    next_neuron = None
    weight = float()

    def __init__(self, previous_neuron: Neuron, next_neuron: Neuron, weight: float, connection_id=None) -> None:
        self.previous_neuron = previous_neuron
        self.next_neuron = next_neuron
        self.weight = weight
        self.connection_id = connection_id
