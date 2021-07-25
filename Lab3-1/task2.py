#! /usr/bin/env python

import argparse

def run(args):
	x1 = args.x1
	x2 = args.x2
	x3 = args.x3
	
	result = x1*x1 + x2*x2 + x3*x3
	print(result)



parser=argparse.ArgumentParser(
	description="Get sum of three integers squared"
)
parser.add_argument(
	"x1",
	help="input integer 1",
	type=int,
)
parser.add_argument(
	"x2",
	help="input integer 2",
	type=int,
)
parser.add_argument(
	"x3",
	help="input integer 3",
	type=int,
)

args=parser.parse_args()
run(args)


