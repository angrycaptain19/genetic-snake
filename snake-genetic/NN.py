import numpy as np

class NN():
  def __init__(self):
    self.fitness = 0
    '''    
    self.w1 = np.random.uniform(-1, 1, size=(10, 15))
    self.w2 = np.random.uniform(-1, 1, size=(15, 20))
    self.w3 = np.random.uniform(-1, 1, size=(20, 10))
    self.w4 = np.random.uniform(-1, 1, size=(10, 3))
    '''
    self.w1 = np.random.randn(10, 10)
    self.w2 = np.random.randn(10, 20)
    self.w3 = np.random.randn(20, 10)
    self.w4 = np.random.randn(10, 3)


  def relu(self, x):
    return np.maximum(0, x)

  def softmax(self, x):
    expo = np.exp(x)
    expo_sum = np.sum(np.exp(x), axis=0)
    return expo/expo_sum
  
  def linear(self, x):
    return x
        
  def forward(self, inputs):
    net = self.relu(np.dot(inputs, self.w1))
    net = self.relu(np.dot(net, self.w2))
    net = self.relu(np.dot(net, self.w3))
    net = self.softmax(np.dot(net, self.w4))
    return net



