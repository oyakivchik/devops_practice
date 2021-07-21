import sys
arg = int(sys.argv[1])
counter = 0
for i in range(arg - 1, 1, -1):
    if (arg % i == 0):
        counter+=1         
print(counter)
