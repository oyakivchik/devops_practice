import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--a", default=1, help="This is the 'a' variable")
parser.add_argument("--b", default=1, help="This is the 'b' variable")
parser.add_argument("--c", default=1, help="This is the 'c' variable")

args = parser.parse_args()

a = int(args.a)
b = int(args.b)
c = int(args.c)
list = [a, b, c]

print(sum(x**2 for x in list))
