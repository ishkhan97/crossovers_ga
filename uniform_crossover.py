import numpy as np
import random
from numpy.random import randint

#single point crossover in genetic algorithm

par1 = np.array([0,0,0,1,1,0,0,0]) #parent1
par2 = np.array([1,1,1,0,0,1,1,1]) #parent2

col = len(par1) #the total num of columns

child1 = np.zeros(col)
child2 = np.zeros(col)

crossing = np.random.rand(col-1) #crossingpoint
print(crossing)

for i in range(len(crossing)):
    if crossing[i] < 0.5:
        temp = par1[i]
        par1[i] = par2[i]
        par2[i] = temp
        child1 = par1
        child2 = par2
        
print(child1)
print(child2)
