#!/usr/bin/python

def search(str, pattern):
	l = len(str)
	l2 = len(pattern)
	matches = []
	for i in xrange(0, l-l2+1): # Going to search after l-l2 does not have any sense because the pattern being longer that the number of words still in the string, will never by found
		if str[i] == pattern[0]:
			found = True
			for j in xrange(1, l2):
				if str[i+j] != pattern[j]:
					found = False
					break
			if found:
				matches.append(i)
	return matches

print "Please enter the string to search into"
str = raw_input()
while True:
	try:
		print "Pattern to search for?"
		print search(str, raw_input())
	except EOFError:
		break
