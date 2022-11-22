from networks import Agent, sigmoid, leakyRelu
import numpy as np
import time

def initModel(n):
    #Creates a list of n base agents for the model with the specified model dimensions
    agents = []
    #initialise the weights
    inputDim = 85
    hidden1Dim = 100
    hidden2Dim = 50
    hidden3Dim = 25
    outputDim = 1

    networkDim = [inputDim, hidden1Dim, hidden2Dim, hidden3Dim, outputDim]
    biases = []

    for i in range(len(networkDim)-1):
        biases.append(np.random.randn(networkDim[i+1]))

    layers = [np.random.randn(i, j) for i, j in zip(networkDim[:-1], networkDim[1:])]

    agent = Agent(layers, biases, leakyRelu)
    agents.append(agent)
    
    myList = list(range(1, 86))
    start = time.perf_counter()
    for i in range(100000):
        agent.feedForward(myList)
    end = time.perf_counter()
    print((end-start) / 100000)
    return agents

def play(player1, player2):
    #plays a game between two agents, returning the gain to each agent in terms of fitness
    pass
    
initModel(100)