import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--x", help="Number x", required=True)
parser.add_argument("--y", help="Number y", required=True)
parser.add_argument("--z", help="Number z", required=True)

args = parser.parse_args()

x=float(args.x)
y=float(args.y)
z=float(args.z)


print((x+y+z)/3.0)
