import numpy
print("Input numbers:")
arr = input()
l = list(map(float,arr.split(' ')))
print(numpy.mean(l))