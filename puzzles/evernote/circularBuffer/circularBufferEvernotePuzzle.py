#!/usr/bin/python
import sys

DBG = False

k = int(raw_input())

if 0 == k:
	# Nothing to do, just read the buffer and escape
	try:
		while raw_input():
			pass
	except EOFError:
		pass
	sys.exit(0)

buff = [""] * k
head = tail = 0
empty = True

def append(el):
	global buff, head, tail, k, empty, DBG
	
	if DBG:
		print "Appending", el
	if tail == head and not empty:
		if DBG:
			print "Buffer full (head=", head, ", tail=", tail, "), removing one entry"
		remove(1)

	buff[tail] = el
	tail = (tail+1) % k
	empty = False

def remove(n):
	global buff, head, tail, k, empty, DBG
	
	for x in xrange(0, n):
		_remove()

def _remove():
	global buff, head, tail, k, empty, DBG
	
	
	if not empty:
		if DBG:
			print "Removing"
		head = (head+1) % k
		if DBG:
			print "Head=", head
		if head == tail:
			empty = True
	

def list_buff():
	global buff, head, tail, k, empty, DBG
	

	if DBG:
		print "List: "

	if empty:
		return

	i = head
	while True:
		print buff[i]
		i = (i+1) % k
		if i == tail:
			break


line = raw_input()
while line:
	tmp = line.split(" ")
	cmd = tmp[0]
	
	if "A" == cmd:
		n = int(tmp[1])
		for x in xrange(0, n):
			append(raw_input())
	elif "R" == cmd:
		n = int(tmp[1])
		remove(n)
	elif "L" == cmd:
		list_buff()
	elif "Q" == cmd:
		break;

	try:
		line = raw_input()
	except EOFError:
		sys.exit(0)

