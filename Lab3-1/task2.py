#! /usr/bin/python3

from sys import argv
from re import match


def sumOfSquares(nums):
    _numbers = []
    _sum = 0

    for num in nums:
        if match('^(\d+|(\d*[.,]?\d+))$', num):
            num = num.replace(',', '.')
            _numbers.append(num)
            _sum += (pow(float(num), 2))

    if len(_numbers):
        print(f'The sum of the squares of the {", ".join(_numbers)} is {_sum}')
    else:
        print('No numeric parameters received')


args = argv[1:] if argv[1:] else 0

print('No parameters received') if args == 0 else sumOfSquares(args)
