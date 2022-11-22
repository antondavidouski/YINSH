from networks import Agent, sigmoid, leakyRelu
import numpy as np
import time
from copy import deepcopy

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
    
    for i in range(n):
        agent = Agent(layers, biases, leakyRelu)
        agents.append(agent)
    
    # myList = list(range(1, 86))
    # start = time.perf_counter()
    # for i in range(100000):
    #     agent.feedForward(myList)
    # end = time.perf_counter()
    # print((end-start) / 100000)
    
    return agents

def play(player1, player2):
    #plays a game between two agents, returning the winner
    pass

def train(epochs, agents):
    # trackFile = open("track.txt", "w") #will be used to track the progress of the model, can be "played back" later to see how model preformed at different stages of training
    for i in range(epochs):
        tournament(agents)
        
def tournament(agents):
    #takes a list of agents and plays a tournament between them, adding fitness to the winners and removing the losers
    currentStage = agents
    startSize = len(currentStage)
    while len(currentStage) > 1:
        nextStage = []
        for i in range(0, len(currentStage), 2):
            winner = play(currentStage[i], currentStage[i+1])
            winner.incrementFitness(2 * (startSize - len(currentStage))) #fitness is incremented by 2 * (start size - number of agents in current stage), ie higher reward is given as you get further in the tournament
            nextStage.append(winner)
        currentStage = nextStage
    currentStage[0].incrementFitness(startSize) #the winner of the tournament gets the highest reward

def main():
    agents = initModel(64) #n must be a power of 2 for the tournament to work
    train(100, agents)

a = [i for i in range(1, 65)]
tournament(a)