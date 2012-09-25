#!/usr/bin/python

"""
Algo description:
The idea is to "rotate" and array from right to left of a given number.
By "rotating" we mean here "shifting with elements going out of the array (<0 or > len(arr)) 
being placed at the other end of the array"

Author: TD
License: GPLv3
"""

DBG = False

def rotate(arr, k):
	def reverse(arr, start, end):
		if DBG:
			print "From",start,"to", start+(end-start)/2
		for x in xrange(start, start+(end-start)/2):
			tmp = arr[x]
			arr[x] = arr[end-x]
			arr[end-x] = tmp
		return arr

	l = len(arr)
	k = k % l
	if DBG:
		print "k=",k
	arr=reverse(arr, 0, k-1)
	if DBG:
		print arr
	arr=reverse(arr, k, l-1)
	if DBG:
		print arr
	arr=reverse(arr, 0, l-1)
	return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8]
print "Before:", arr
print "After:", rotate(arr, 4)
