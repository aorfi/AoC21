import re
instruct = open('D2Input.txt','r').read().splitlines()

# Part 1
# forward = [int(re.search(r'\d+', x).group()) for x in instruct if 'forward' in x]
# down = [int(re.search(r'\d+', x).group()) for x in instruct if 'down' in x]
# up = [int(re.search(r'\d+', x).group()) for x in instruct if 'up' in x]
# hor = sum(forward)
# depth = sum(down)-sum(up)
# final = hor*depth


# Part 2
hor = 0
depth = 0
aim = 0
for i in instruct:
    value = int(re.search(r'\d+', i).group())
    if "forward" in i:
        hor += value
        depth += value*aim
    if "down" in i:
        aim += value
    if "up" in i:
        aim -= value
print(hor*depth)


