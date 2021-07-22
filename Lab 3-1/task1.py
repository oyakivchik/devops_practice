from itertools import * #iterators module

for i in permutations('masha'): 
    res = ''    
    for j in i:
        result = res + j 
    print(res)