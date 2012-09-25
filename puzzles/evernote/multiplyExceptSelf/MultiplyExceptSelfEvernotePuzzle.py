#!/usr/bin/python

n = int(raw_input())

l = [0] * n
prod = 1
nOfZeros = 0
positionOfLastZero = -1
for i in xrange(0, n):
	a = int(raw_input())
	if 0 == a:
		nOfZeros += 1
		if nOfZeros > 1:
			break
	else:
		prod *= a # We do not count the zeros in the product so that we are able to get the product without the zero for itself (for all the other ones if will be... 0, anyway !)
	l[i] = a
	

if nOfZeros > 1: # Only zeros...
	for x in xrange(0, n):
		print 0
else: # Means we only have ONE zero or none
	for e in l:
		if 0 == e:
			print prod
		elif nOfZeros == 1:
			print 0
		else:
			print prod/e