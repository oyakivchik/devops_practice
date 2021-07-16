import itertools
letters = ['a', 'e', 'i', 'o', 'u']
for L in range(0, len(letters)+1):
    for words in itertools.permutations(letters, L):
        if (len(words)!=5):
            continue
        else:
            print(words)
