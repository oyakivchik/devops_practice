from itertools import *

for i in permutations('aeiou'): #Проходимося по заданому набору літер
    res=''    
    for c in i:
        res=res+c #Додаємо в один рядок
    print(res) #Виводимо результат
