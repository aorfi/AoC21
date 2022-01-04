import numpy as np
from numpy import loadtxt
data = loadtxt("D1Input.txt", comments="#", delimiter="\n", unpack=False)

# # Part 1
# counter = 0 
# for i in range(len(data)-1):
#     if data[i] < data[i+1]:
#         counter += 1
# print(counter)


# Part 2
slinding = []
for i in range(len(data)-2):
    sum = data[i]+data[i+1]+data[i+2]
    slinding.append(sum)
sliding_counter = 0
for i in range(len(slinding)-1):
    if slinding[i]<slinding[i+1]:
        sliding_counter +=1
print(sliding_counter)