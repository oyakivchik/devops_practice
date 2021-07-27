n = input('Enter your number:')
print('Number of dividers ')
i = 1
a = []
while i ** 2 <= n:
    if n % i == 0:
        a.append(i)
        if i != n // i:
            a.append(n // i)
    i += 1
a.sort()
print(a)


print('Second part')
x1 = input('x1:')
x2 = input('x2:')
x3 = input('x3:')
print('Arithmetic mean ')
print((x1+x2+x3)/3)
