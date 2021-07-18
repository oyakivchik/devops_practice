from itertools import * #iterators module

for i in permutations('ivanko'): 
    result = ''    
    for j in i:
        result = result + j #concat
    print(result)