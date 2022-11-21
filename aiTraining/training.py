from neuralNetworks import Agent, sigmoid
import numpy as np

def initModel(n):
    #Crrates a list of n base agents for the model with the specified model dimensions
    
    #initialise the weights
    inputDim = 10
    hidden1Dim = 100
    hidden2Dim = 50
    hidden3Dim = 25
    outputDim = 1

    networkDim = [inputDim, hidden1Dim, hidden2Dim, hidden3Dim, outputDim]
    biases = []

    for i in range(len(networkDim)-1):
        biases.append(np.random.randn(networkDim[i+1]))

    layers = [np.random.randn(i, j) for i, j in zip(networkDim[:-1], networkDim[1:])]

    agent = Agent(layers, biases, sigmoid)
    myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(agent.feedForward(myList))
