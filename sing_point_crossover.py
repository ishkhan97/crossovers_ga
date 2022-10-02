import numpy as np
import random

#single point crossover in genetic algorithm

par1 = np.array([0,0,0,1,1,0,0,0]) #parent1
par2 = np.array([1,1,1,0,0,1,1,1]) #parent2

col = len(par1) #the total num of columns

child1 = np.zeros(col)
child2 = np.zeros(col)

crossing = random.randint(2, col-1) #crossingpoint
print(crossing)

for i in range(col):
    if i < crossing:
        child1[i] = par1[i]
        child2[i] = par2[i]
    else:
        child1[i] = par2[i]
        child2[i] = par1[i]
        
print(child1)
print(child2)
