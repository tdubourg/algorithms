#!/usr/bin/python

"""Says wether or not a given array holds a subset that sums up to s (here we use it for sum=0) 
Author: TD
Date: 24/09/12
License: GPLv3
"""

# T is an addition to the algorithm from Wikipedia, serves as a tracking purpose (we want to know the subset)
T = {}

# Straight from Wikipedia
def Q(i, s, N, P, arr):
	global T
	if i <= 0:
		result = (arr[0] == s)
		if result:
			T[i] = True # keep track of which one was chosen
	elif s < N or s > P:
		result = False
	else:
		subresult = (arr[i] == s)
		if subresult:
			T[i] = True # keep track of which one was chosen
			return True
		subresult2 = Q(i-1, s-arr[i], N, P, arr)
		if subresult2:
			T[i] = True # keep track of which one was chosen
			return True
		result = (subresult or subresult2 or Q(i-1, s, N, P, arr)) # Changed the order of 

	return result

def Sums(arr, l):
	N =0
	P=0
	for i in xrange(0, l):
		if arr[i] < 0:
			N += arr[i]
		else:
			P += arr[i]
	return N,P

# arr = [5, 6, -7, 9, 55, -32, -18, 2]

# arr = [5, 6, -14, -28, 17, -1]


# Test that stuff:
MAX_ELEM = 50
N_TEST = 10
MAX_VALUE = 10000
if __name__ == '__main__':
	fails = 0
	import random, time
	random.seed()
	Times = {}
	for x in xrange(1, N_TEST):
		print "Launching test N", x
		max = random.randint(1, MAX_ELEM)
		print "Generating", max, "values..."
		arr = []
		for y in xrange(0, max):
			arr.append(random.randint(-MAX_VALUE, MAX_VALUE))
		print "Preparing tracking system"
		l = len(arr)
		T = {i:None for i in xrange(0, l)} # Init the storage for already computed values
		
		print "Summing..."
		N, P = Sums(arr, l)
		
		print "Solving..."
		a = time.time()
		res = Q(l-1, 0, N, P, arr)
		b = time.time()
		Times[max] = b-a

		# print res
		# print T
		if res:
			sum = 0
			for i,v in T.items():
				if v:
					# print arr[i],
					sum += arr[i]
			if 0 != sum:
				fails += 1
				print "An error in the tracking system has been detected"
			print
			print "Sum=", sum

	print "Executed", N_TEST, "tests,", fails, "failed,", (N_TEST - fails), "succeeded."
	print "Times are (in seconds): "
	for n in Times:
		print n, ":", '%0.6f' % Times[n]