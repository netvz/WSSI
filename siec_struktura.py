import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow


#funkcja aktywacji neuronow - relu
def relu(x): 
    return max(x*.1, x)   
    
#funkcja aktywacji koncowej warstwy - sigmoid
def sigmoid(x):
    return 1 / 1 + np.exp(-x)


class Neuron:  
    def __init__(self, n_inputs, activation, bias = 0., weights = None):  
        self.activation = activation
        self.b = bias
        if weights: self.ws = np.array(weights)
        else: self.ws = np.random.rand(n_inputs)
        
    #funkcja liczaca output pojedynczego neuronu
    def __call__(self, xs): 
        return self.activation(xs @ self.ws + self.b) 


class Layer: 
    def __init__(self, neurons, inputs, activation, bias = 0., weights = None):
        self.neurons = [Neuron(inputs, activation, bias, weights) for i in range(neurons)]
    
    def __call__(self, inputs):
        return np.array([neuron(inputs) for neuron in self.neurons])
    

class Network:
    def __init__(self, n_inputs, layer_specs):  
        self.layers = []
        n_inputs_next_layer = n_inputs
        self.layer_sizes = []
        self.layer_sizes.insert(0, n_inputs)

        for layer_spec in layer_specs:
            n_neurons, activation, bias, weights = layer_spec
            self.layers.append(Layer(n_neurons, n_inputs_next_layer, activation, bias, weights))
            n_inputs_next_layer = n_neurons
            self.layer_sizes.append(n_neurons)


    def __call__(self, inputs):
        output = inputs
        for layer in self.layers:
            output = layer(output)
        return output


    #funkcja wyswietlajaca siec w zaleznosci od jej konstrukcji 
    def generate_view(self): 
        fig, ax = plt.subplots()

        previous_layer = []

        for layer_index, layer_width in enumerate(self.layer_sizes):
            neuron_layer = []
            spacing_x = 1.0 / (len(self.layer_sizes) + 1)
            spacing_y = 1.0 / (layer_width + 1)
            
            for i in range(layer_width):  
                neuron_position = ((layer_index + 1) * spacing_x, (i + 1) * spacing_y)
                neuron_layer.append(neuron_position)
                circle = plt.Circle(neuron_position, 0.05, edgecolor='black', facecolor='pink', zorder=4)  # fixed size
                ax.add_artist(circle)

                if previous_layer:
                    for prev_neuron_pos in previous_layer:
                        arrow = FancyArrow(prev_neuron_pos[0], prev_neuron_pos[1],
                                        neuron_position[0] - prev_neuron_pos[0],
                                        neuron_position[1] - prev_neuron_pos[1], width=0.002, color='gray', zorder=0)
                        ax.add_artist(arrow)

            previous_layer = neuron_layer

        ax.set_aspect('equal')
        plt.axis('off')
        plt.show()



network = Network(3, [
    (4, relu, 0.0, None),  
    (4, relu, 0.0, None),  
    (1, sigmoid, 0.0, None)  
])

network.generate_view()

