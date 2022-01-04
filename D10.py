from functools import reduce
import numpy as np

data = open('D10Input.txt','r').read().splitlines()
print(data)


# Part 1
open_brackets = list("({[<")
closed_brackets = list(")}]>")
point_mapping = [3,1197,57,25137]
points = 0
for brackets in data: 
    reduced_brackets = []
    for i in brackets:
        if i in open_brackets:
            reduced_brackets.append(i)
        elif i in closed_brackets:
            open_index = open_brackets.index(reduced_brackets[-1])
            closed_index = closed_brackets.index(i)
            if open_index == closed_index:
                reduced_brackets.pop(-1)
            else:
                points += point_mapping[closed_index]
                break       
print(points)

# Part 2


open_brackets = list("({[<")
closed_brackets = list(")}]>")
point_mapping = [1,3,2,4]
points = []
for brackets in data: 
    reduced_brackets = []
    for i in brackets:
        if i in open_brackets:
            reduced_brackets.append(i)
        elif i in closed_brackets:
            open_index = open_brackets.index(reduced_brackets[-1])
            closed_index = closed_brackets.index(i)
            if open_index == closed_index:
                reduced_brackets.pop(-1)
            else:
                # points += point_mapping[closed_index]
                break     
    else:
        points.append(reduce(lambda x,y: 5*x + point_mapping[open_brackets.index(y)], reduced_brackets[::-1], 0))
        # print(reduce(lambda x,y: 5*x + point_mapping[open_brackets.index(y)], reduced_brackets[::-1], 0))  
print(np.median(np.array(points)))


