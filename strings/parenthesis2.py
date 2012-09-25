#!/usr/bin/python

"""
Author: TD
License: GPLv3
"""

def printparenthesis(l, r, s):
	if 0 == r:
		print s
		return
	
	if l>0: # still at least one parenthesis open (else nothing to do, just close the open ones)
		printparenthesis(l-1, r, s+"(") # launch the process with an open parenthesis at the front
		
		# if l < r: # do we have at least one parenthesis that we can try to close?
		# 	printparenthesis(l, r-1, s+")") # launch the process with a closed parenthesis at the front
	if l < r:
		printparenthesis(l, r-1, s+")") # no open parenthesis left BUT closed ones still (else we would have stopped on first line of the function)
	
	
printparenthesis(2,2,"")
print ""
printparenthesis(3,3,"")
print ""
printparenthesis(4,4,"")

