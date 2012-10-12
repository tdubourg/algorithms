#!/usr/bin/python

import sys
from math import ceil
sys.path.insert(0, '../../sorts/')

from heap_sort_in_place_and_on_subarray import *

DBG = True

def find_kth(arr, k):
	l = len(arr)
	if DBG:
		print "Looking for the ", k, "-th element in an array of length", l
	end = l-1
	if l < 6: # If the array is small enough, sort it (using heapsort for instance)
		heapsort(arr, 0, end)
		return arr[int(ceil(l/2.0))] # return median
	else: # Else, cut it into pieces of 5 and sort those pieces
		i = 0
		medians = []
		while (i+5) < end:
			if DBG:
				print "current interval=[", i, ",", i+4, "]"
			heapsort(arr, i, i+4)
			medians.append(arr[i+2]) # grab the third element, which is the median of this subarray
			i += 5
		if DBG:
			print "final interval=[", i, ",", end, "]"
		heapsort(arr, i, end) # the last piece
		medians.append(arr[int(ceil((l-i)/2.0))])

		if DBG:
			print "Medians found: ", medians

		l2 = len(medians)
		m = find_kth(medians, int(ceil(l2/2.0)))

		if DBG:
			print "Median of medians found m=", m

		L = []
		R = []

		# Length of the lists, will avoid using len()
		lL = 0
		lR = 0
		lM = 0

		for x in xrange(0, l):
			if arr[x] < m:
				L.append(arr[x])
				lL += 1
			elif arr[x] > m:
				R.append(arr[x])
				lR += 1
			else:
				lM += 1

		if DBG:
			print "L=", L, "size =", lL
			print "R=", R, "size =", lR

		if k <= lL:
			return find_kth(L, k)
		elif k > (lL + lM):
			return find_kth(R, k-(lL + lM))
		else:
			return m



test = [1, -1, 5, 7, 3, 6, 290, 2, -12, 649, 13, 9, -315, 59, 269093]
l = len(test)
k = int(ceil(l/2.0))
print l
print find_kth(test, k)

# Check by sorting + returning the k-th:
print heapsort(test, 0, l-1)
print test[k-1]
