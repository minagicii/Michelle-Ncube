import random

counterone = 0
countertwo = 0
counterthree = 0
counterfour = 0
counterfive = 0
countersix = 0
n = 100000

for i in range (n) : 
 number = random.randint (1, 6)
 print (number) 
 if number == 1:
    counterone += 1
 elif number == 2:
    countertwo += 1
 elif number == 3:
    counterthree += 1
 elif number == 4:
    counterfour += 1
 elif number == 5:
    counterfive += 1
 elif number == 6:
    countersix += 1

print ("1 was rolled", counterone, "times", "which is", (counterone/n)*100, "% of the time")
print ("2 was rolled", countertwo, "times", "which is", (countertwo/n)*100, "% of the time")
print ("3 was rolled", counterthree, "times", "which is", (counterthree/n)*100, "% of the time")
print ("4 was rolled", counterfour, "times", "which is", (counterfour/n)*100, "% of the time")
print ("5 was rolled", counterfive, "times", "which is", (counterfive/n)*100, "% of the time")
print ("6 was rolled", countersix, "times", "which is", (countersix/n)*100, "% of the time")