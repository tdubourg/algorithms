#!/usr/bin/python

"""
(facebook interview question)
Problem statement: 
Assuming a mapping between numbers and letters, starting at 0 (that is to say, 0=a, 1=b, and so on),
print all the possible translation of a given input integer.
author: TD
"""

ORD0 = ord('a')

def translate(prefix, string, i):
	l = len(string)
	if i >= l:
		print prefix
		return
	
	n = int(string[i])
	translate(prefix+chr(ORD0+n), string, i+1)

	if i+1 < l:
		n = int(string[i])*10 + int(string[i+1])
		translate(prefix+chr(ORD0+n), string, i+2)

while True:
	try:
		translate("", raw_input(), 0)
	except EOFError:
		break