import sys

x1=int(sys.argv[1])
x2=int(sys.argv[2])
x3=int(sys.argv[3])
y = (x1+x2+x3)/3
y = round(y,3)
print(f'average:{y}')
