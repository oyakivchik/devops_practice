import sys

a=int(sys.argv[1]) # Забираємо вхідні дані
b=int(sys.argv[2])
c=int(sys.argv[3])
m=(a+b+c)/3 #Рахуємо медіану
print('Mediana for (%d,%d,%d): %g' % (a,b,c,m)) #Виводимо результат
