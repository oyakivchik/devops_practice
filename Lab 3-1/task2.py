import sys

#get input data
a =int(sys.argv[1]) 
b =int(sys.argv[2])
c =int(sys.argv[3])

#median
m = (a + b + c) / 3

#sum of squares 
s = a**2 + b**2 + c**2

print('Median (%d, %d, %d): %g' % (a, b, c, m)) 
print('Square sum (%d, %d, %d): %d' % (a, b, c, s))