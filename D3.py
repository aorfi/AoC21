import numpy as np
from numpy import loadtxt
data = loadtxt("D1Input.txt", comments="#", delimiter="\n", unpack=False)
print(data)