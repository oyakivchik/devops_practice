from itertools import permutations


def function(array):
	for i in permutations(array):
		print("".join(i))


array = ['a' , 'e' , 'i' , 'o' , 'u']
function(array) 
