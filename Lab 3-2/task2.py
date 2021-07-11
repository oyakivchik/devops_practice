print("input numbers: ")
x1, x2, x3 = [int(i) for i in input().split()]
y = (x1+x2+x3)/3
y = round(y,3)
print(f'average:{y}')
