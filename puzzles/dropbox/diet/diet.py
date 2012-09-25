#!/usr/bin/python

"""
Dropbox Diet challenge. Using subset sum algorithm
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

if __name__ == '__main__':
        Names = {}
        n = int(raw_input())
        arr = [0] * n
        T = {i:None for i in xrange(0, n)} # Init the storage for already computed values
        for i in xrange(0, n):
            try:
                name, num = raw_input().strip().split(" ")
                num = int(num)
                arr[i] = num
                Names[i] = name # Using i against num to be able to handle multiple things with the same caloric integer
            except EOFError:
                break
        N, P = Sums(arr, n)
        
        res = Q(n-1, 0, N, P, arr)

        if not res:
            print "no solution"
        else:
            for k,v in T.items():
                if v is not None:
                    print Names[k]
