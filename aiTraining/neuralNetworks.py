import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

class Agent:
    
    def __init__(self, inputSize, hidden1, hidden2, outputSize, oldWeights1, oldWeights2, oldWeights3):
        self.inputSize = inputSize
        self.hidden1 = hidden1
        self.hidden2 = hidden2
        self.outputSize = outputSize
        self.oldWeights1 = oldWeights1
        self.oldWeights2 = oldWeights2
        self.oldWeights3 = oldWeights3
        self.weights1, self.weights2, self.weights3 = self.generateNewWeights(self.oldWeights1, self.oldWeights2, self.oldWeights3)
        print(self.weights1)
        print(self.weights2)
        print(self.weights3)
    
    def generateNewWeights(self, oldWeights1, oldWeights2, oldWeights3):
        #will write this later, currently doesnt do anything useful
        self.weights1 = oldWeights1
        self.weights2 = oldWeights2
        self.weights3 = oldWeights3
        return self.weights1, self.weights2, self.weights3
        
    def evaluate(self, inputs):
        self.layer1 = sigmoid(np.dot(inputs, self.weights1))
        self.layer2 = sigmoid(np.dot(self.layer1, self.weights2))
        self.output = sigmoid(np.dot(self.layer2, self.weights3))
        return self.output


#just testing that stuff works here
#initialise the weights
random1 = np.ones((1,3))
random2 = np.ones((3,3))
random3 = np.ones((3,1))
agent = Agent(1, 3, 3, 1, random1, random2, random3)
print(agent.evaluate(np.array([1])))
    
    