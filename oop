
import random
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

max = 0
min = 0
all_results = []

for i in range(2000): # 2000 random walks/trials
    position = 0

    if i%100 == 0:
        print("Running simulation ", i, " of 2000") # iteratively checks if every 100th trial has been completed, printing progress to the terminal

    for j in range (200): # 200 steps in each walk/trial
        step = random.randint(0,1) # randomly generates numbers '0' or '1'
        if step == 0:
            position += 1
        elif step == 1:
            position += -1 

        if position > max :
                max = position 
        elif position < min :
                min = position

    all_results.append(position)
    all_results.sort()

# plotting the histogram displaying final positions of the random walks

plt.hist(all_results, edgecolor= 'black', bins=30)
plt.title("1D Random Walk Histogram")
plt.xlabel("Final Position")
plt.ylabel("Frequency of Final Positions")

# statistics
print('sample mean:', np.mean(all_results))
print('sample standard deviation:', np.std(all_results))
print('Min position: ', min)
print('Max position: ', max)
plt.show()
