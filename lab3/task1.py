import random as r
import os
os.getcwd()
import sys
sys.path.append('py-linq-1.3.0')
sys.path.append('six-1.16.0')
from py_linq import Enumerable


def strichka():
    chars = ['a', 'e', 'i', 'o', 'u']
    new_string = ''
    new_strings = []
    for i in range(0, 10000):
        strings1 = chars.copy()
        new_string = ''
        for char in chars:
            randdig = r.randint(0, len(strings1) - 1)
            new_string += strings1[randdig]
            strings1.remove(strings1[randdig])
        new_strings.append(new_string)
    res = sorted(Enumerable(new_strings).distinct())
    for i in range(0, len(res)):
        print(res[i], end="\n")


strichka()
