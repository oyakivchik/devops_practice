from itertools import *

for i in permutations('aeiou'):
	comb=''
	for e in i:
		comb += e
	print(comb)
