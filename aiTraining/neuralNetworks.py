import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

class Agent:
    
    def __init__(self, layers, biases, activation):
        #layers is a 2D array of numpy arrays, each array is a layer of the network, likewise for biases
        self.layers = layers
        self.biases = biases
        self.activation = activation
        self.layers, self.biases = self.generateNewWeights(self.layers, self.biases)
    
    def generateNewWeights(self, layers, biases):
        #will write this later, currently doesnt do anything useful
        self.newLayers = layers
        self.newBiases = biases
        return self.newLayers, self.newBiases
        
    def feedForward(self, inputs):
        #feed forward through the network
        self.output = inputs
        for weights, bias in zip(self.layers, self.biases):
            self.output = self.activation(np.dot(self.output, weights) + bias)
        return self.output

