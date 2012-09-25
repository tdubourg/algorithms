#!/usr/bin/python

"""
Author: TD
License: GPLv3
"""

four = [float('-inf')] * 5

def try_insert(a):
    global four

    four[4] = a # Note : This index is not in the "top four", it's here because it's handy
    i = 3
    while a > four[i] and i >= 0:
        # Swap values:
        tmp = four[i]
        four[i] = four[i+1]
        four[i+1] = tmp
        # Decrement:
        i -= 1

# Grab number of lines:
n = int(raw_input())

if n <= 4: # Less than the required number in the "top" list... just have to print them << Note: We do not need to sort them because the instructions does not ask for printing in the growing order !
    for x in xrange(0, n):
        print raw_input()
else:
    for x in xrange(0, n):
        try_insert(int(raw_input()))
    
    print four[0]
    print four[1]
    print four[2]
    print four[3]