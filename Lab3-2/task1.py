import sys

if __name__ == "__main__":
	numb = int(sys.argv[1])
	count = 0
	for i in range(numb - 1, 1, -1):
    		if (numb % i == 0):
        		count += 1
	print (count)