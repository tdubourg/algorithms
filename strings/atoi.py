#!/usr/bin/python


def atoi(str):
	maxTenPower = len(str)
	if '-' == str[0]:
		negative = True
		start = 1
	else:
		negative = False
		start = 0
	sum = 0
	ord0 = ord('0')
	for i in xrange(start, maxTenPower):
		sum += pow(10, i-start) * (ord(str[maxTenPower-1-i])-ord0)

	if negative:
		return (-1*sum)
	else:
		return sum

print "Please write a number"
print atoi(raw_input())