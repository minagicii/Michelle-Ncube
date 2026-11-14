import numpy as np
from numpy import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x = np.random.randint(0,2, size =(2000,200))
y = np.zeros((2000,1))

transform_x = 2*x - 1
new_array = np.concatenate((y, transform_x), axis = 1) #renders starting position for each trial to be zero
steps = np.cumsum(new_array, axis = 1) 
 
threshold = int(input("Enter threshold value: ")) #value where the position of walk is 'ruined'
broadcast = steps <= threshold
collapsed = np.any(broadcast, axis = 1)

ruin_probability = np.mean(collapsed)*100

data = np.array(steps[:,-1]) 

# plotting the histogram displaying final positions of the random walks
plt.hist(data, edgecolor= 'black', bins=30)
plt.title("1D Random Walk Histogram")
plt.xlabel("Final Position")
plt.ylabel("Frequency of Final Positions")

# statistics
print('sample mean:', np.mean(data))
print ("Ruin probability: ", ruin_probability)
print('sample standard deviation:', np.std(data))
print('Min position: ', min(data))
print('Max position: ', max(data))
plt.show()