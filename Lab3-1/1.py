  
#! /usr/bin/python

from itertools import permutations


def perm(arr):
    for c in permutations(arr):
        print(''.join(c))


chars = ['a', 'e', 'i', 'o', 'u']
perm(chars)