#!/usr/bin/python

"""
Author: TD
License: GPLv3
"""


import math
# Newton's iterative method

def sqrt(a, precision):
	if 1 == a:
		return 1
	if 0 == a:
		return 0

	if a < 0:
		return float('nan')

	r = 1
	old_r = r
	while True:
		old_r = r
		r = 0.5 * (r + a/r)
		if (r*r) == a: # "exact" sqrt found
			print "Stopping by exactness"
			return r
		if math.fabs(old_r-r)<=precision:
			print "Stopping by precision reached"
			return r


print "Please tell us the precision to use for sqrt() results"
precision = float(raw_input())

while True:
	print "Number?"
	print sqrt(float(raw_input()), precision)