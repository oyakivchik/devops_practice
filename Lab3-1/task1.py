#! /usr/bin/env python

letters = ['a', 'e', 'i', 'o', 'u']
result = []

for el_0 in letters:
    result.append(el_0)
for el_0 in letters:
    for el_1 in letters:
        if(el_0!=el_1):
            result.append(el_0 + el_1)
for el_0 in letters:
    for el_1 in letters:
        for el_2 in letters:
            if(el_0!=el_1 and el_0!=el_2 and el_1!=el_2):
                result.append(el_0 + el_1 + el_2)
for el_0 in letters:
    for el_1 in letters:
        for el_2 in letters:
            for el_3 in letters:
                if(el_0!=el_1 and el_0!=el_2 and el_1!=el_2
                    and el_0!=el_3 and el_1!=el_3 and el_2!=el_3):
                    result.append(el_0 + el_1 + el_2 + el_3)
for el_0 in letters:
    for el_1 in letters:
        for el_2 in letters:
            for el_3 in letters:
                for el_4 in letters:
                    if(el_0!=el_1 and el_0!=el_2 and el_1!=el_2
                        and el_0!=el_3 and el_1!=el_3 and el_2!=el_3
                        and el_0!=el_4 and el_1!=el_4
                        and el_2!=el_4 and el_3!=el_4):
                        result.append(el_0 + el_1 + el_2 + el_3 + el_4)

# print ("Result of length [", len(result), "]:")
for el in result:
    print (el)
