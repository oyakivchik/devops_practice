from itertools import permutations 
for x in permutations('aeiou'):
        sample=''
        for z in x:
                sample += z
        print(sample)
