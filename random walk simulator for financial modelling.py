import random 

above = 0
below = 0
equal = 0
max = 0
min = 0

all_results = []

for i in range(100):
    position = 0

    for j in range (100):
        step = random.randint(0,1)
        if step == 0:
            position += 1
        elif step == 1:
            position += -1 

        if position > max :
                max = position 
        elif position < min :
                min = position
        
    if position > 0 :
        above += 1
    elif position < 0 :
        below += 1 
    else : 
        equal += 1

    all_results.append(position)
    all_results. sort()

bottom = all_results [5]
top = all_results [95]


print(" Position :" , str(position))
print ("Ended above zero: ", above, " times")
print ("Ended below zero: ", below, " times")
print ("max position: ", max)
print ("min position: ", min)
print ("All results: ", all_results)
print ("Bottom 5%: ", bottom)
print ("Top 5%: ", top)
print ("95% of the time, the position is between ", bottom, " and ", top)
