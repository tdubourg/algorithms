#!/usr/bin/python

def itoa(i):
	n = 0

	if 0==i:
		return "0"
	
	if i > 0:
		comp = 1
		while i >= comp:
			n += 1
			comp *= 10
	else:
		comp = -1
		while i <= comp:
			n += 1
			comp *= 10

	n -= 1 # Because we do >= and <= comparisons then we need to substract one BUT it avoids thinking about "is i beginning with a 1? With a 9?" Here we are sure we were at the next power of ten and we substract one
	
	# We now have the length of the number in n
	# if we were in C we would allocate a char[n] buffer now...
	if i < 0:
		res = "-"
		i *= -1
	else:
		res = ""

	divider = pow(10, n)
	ord0 = ord('0')
	for x in xrange(0, n+1):
		res += chr(i/divider + ord0)
		i -= (i/divider) * divider # IS NOT equal to x, will floor() in the middle...
		divider /= 10
	return res


print "Please write a number"
print itoa(int(raw_input()))
		
