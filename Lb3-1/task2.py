#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys

a=int(sys.argv[1]) # Забираємо вхідні дані
b=int(sys.argv[2])
c=int(sys.argv[3])
m=(a+b+c)/3 #Рахуємо медіану
s=a**2+b**2+c**2 #Рахуємо суму квадратів
print('Mediana for (%d,%d,%d): %g' % (a,b,c,m)) #Виводимо результат медіани
print('Square sum for (%d,%d,%d): %d' % (a,b,c,s)) #Виводимо результат суми квадратів
