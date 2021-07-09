
from itertools import combinations

symbols = "aeiou"

max_length = len(symbols)

for length in xrange(1, max_length + 1):
    for word in map(''.join, combinations(symbols, length)):
        print word
