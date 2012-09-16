#!/usr/bin/python

# Explanation about this one because the "title" is not obvious:
# We are looking for the minimum continous set of numbers in an array (continuous = from a given index
# to another one without skipping some indice) that forms the maximum sum

def max_sum(arr):
	maxSum = curr_start = start = end = tmpSum = 0 # null-them-all

	l = len(arr)
	for i in xrange(0, l):
		# Here we have "start" and "end" indice that will tell us the indice for the final
		# subset that forms the max sum
		# But we also have a curr_start that is used to
		# know where the currently evalutated subset started
		# the "curr_end" variable is in fact i, the current index !
		
		if tmpSum <= 0: # previous numbers took us down to zero, then skip them (they will anyway have no POSITIVE impact on the sum)
			curr_start = i
		
		tmpSum += arr[i]
		
		if tmpSum > maxSum:
			maxSum = tmpSum
			start = curr_start
			end = i

	return (start, end, maxSum)


print "Please type an space-separated-values integer list"
print max_sum([int(_) for _ in raw_input().split(" ")])