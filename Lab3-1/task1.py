from itertools import *

for i in permutations('aeiou'): 
    result=''    
    for s in i:
        result=result+s 
    print(result) 