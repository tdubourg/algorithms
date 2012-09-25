#!/usr/bin/python

"""
Author: TD
License: GPLv3
"""

def upper(s):
	l = len(s)
	s2 = [c for c in s]
	for c in xrange(0, l):
		if s2[c] != " ":
			s2[c] = chr(ord(s2[c]) & (127-32))
	return "".join(s2)
	
	
print "Type your string:"
s = raw_input()

print "Uppercased:"
print upper(s)