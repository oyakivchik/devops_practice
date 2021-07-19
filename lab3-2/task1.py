import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--x", help="Number", required=True)

args = parser.parse_args()
d=1
x=int(args.x)
for number in range(1,x):
    if x%number==0:
        d+=1

print(d)
