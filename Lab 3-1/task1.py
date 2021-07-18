from itertools import * #iterators module

for i in permutations('abcdif'): 
    res = ''    
    for j in i:
        result = res + j 
    print(res)