i = int(input('Input number: '))
c = []
count = 0
for j in range(1, int(i ** 0.5) + 1):
    if i % j == 0:
        count += 1
if float(i ** 0.5) != int(i ** 0.5):
    c.append( 2 * count)
else:
    c.append( 2 * count - 1)
 
print(*c)