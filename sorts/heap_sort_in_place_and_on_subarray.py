#!/usr/bin/python

"""
Author: TD
License: GPLv3

This file contains a Python implementation of heapsort. This implementation has the particularity of allowing to sort only
a given part of the array (in other words: sort a subarray inside the array) with the start and end paxameters

"""

DBG_MSORT = False

def LEFT(i):
	return 2*(i)+1

def RIGHT(i):
	return 2*(i)+2

def get(arr, start, i):
	return arr[i+start]

def _set(arr, start, i, val):
	arr[start+i] = val

def max_heapify(arr, i, size, start):
	global DBG_MSORT
	if DBG_MSORT:
		print "input=", arr
		print i, LEFT(i), RIGHT(i)

	left = LEFT(i)
	right = RIGHT(i)
	parent = i

	if left < size and get(arr, start, left) > get(arr, start, parent):
		parent = left

	if right < size and get(arr, start, right) > get(arr, start, parent):
		parent = right

	if i != parent:
		swap(arr, i, parent, start)
		if DBG_MSORT:
			print "output=", arr
	
		max_heapify(arr, parent, size, start)

def swap(arr, i, j, start):
	tmp = get(arr, start, i)
	_set(arr, start, i, get(arr, start, j))
	_set(arr, start, j, tmp)

def heapsort(arr, start, end):
	x = (end-start)/2
	size = end+1 - start

	if DBG_MSORT:
		print "size=", size
	while x >= 0:
		if DBG_MSORT:
			print "x:", x
		max_heapify(arr, x, size, start)
		x -= 1

	if DBG_MSORT:
		print "===== SECOND LOOP ====="
	
	x = size-1

	while x >= 0:
		if DBG_MSORT:
			print "x:", x
		swap(arr, 0, x, start)
		max_heapify(arr, 0, x, start)
		x -= 1

	return arr


# test = [1, 5, 7, 3, 6, 290, 2, -12, 649, 13, 9, -315, 59, 269093]
# print len(test)
# print heapsort(test, 5, len(test)-3)