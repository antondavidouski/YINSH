import numpy as np

def sigmoid(x):
    np.seterr( over='ignore' )
    return 1.0/(1+np.exp(-x))

def leakyRelu(x):
    return np.maximum(0.01*x, x)

mutationRate = 0.1

class Agent:
    
    def __init__(self, layers, biases, activation):
        #layers is a 2D array of numpy arrays, each array is a layer of the network, likewise for biases
        self.layers = layers
        self.biases = biases
        self.activation = activation
        self.layers, self.biases = self.generateNewWeights(self.layers, self.biases)
        self.fitness = 0
        
    def generateNewWeights(self, layers, biases):
        #make random mutations to the weights and biases
        for i in range(len(layers)):
            for j in range(len(layers[i])):
                for k in range(len(layers[i][j])):
                    if np.random.random() < mutationRate:
                        layers[i][j][k] = np.random.randn()
        for i in range(len(biases)):
            for j in range(len(biases[i])):
                if np.random.random() < mutationRate:
                    biases[i][j] = np.random.randn()
        self.newLayers = layers
        self.biases = biases
        return self.newLayers, self.newBiases
        
    def feedForward(self, inputs):
        #feed forward through the network
        self.output = inputs
        for weights, bias in zip(self.layers, self.biases):
            self.output = self.activation(np.dot(self.output, weights) + bias)
        return self.output

    def increaseFitness(self, n):
        self.fitness += n

