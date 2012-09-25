#!/usr/bin/python

"""
Author: TD
License: GPLv3
"""

import Queue
DBG = False
# Priority queue holding the distances as the key and the node as the value (thus the nearest node is the one on the top)
dist = Queue.PriorityQueue() # inf size

INFTY = float('inf')

G = {
	0: {1: 30, 2: 30, 3: 10},
	1: {0: 30},
	2: {0: 30, 3: 5, 4: 9, 5: 1},
	3: {2: 5, 4: 80, 0: 10, 5: 10},
	5: {2: 1, 4: 1, 3: 10},
	4: {3: 80, 2: 9, 5: 1}
}

def Dijkstra(Graph, source, target):
	global INFTY, DBG
	previous = {}
	distances = {}

	def dist_between(u, v):
		if DBG:
			print "Asking dist(",u,",",v,")"
		return Graph[u][v]
		
	def get_distance(u):
		try:
			return distances[u]
		except KeyError:
			return INFTY
	
	# --- Init --- 
	for v in Graph: 
	   	if v != source:
			distances[v] = INFTY
			dist.put((INFTY, v))
		previous[v] = None
	dist.put((0, source));
	distances[source] = 0
	# --- /Init --- 

	while not dist.empty():
		u = dist.get()
		if DBG:
			print "Current u=",u

		if u[1] == target:
			if DBG:
				print "Found!"
			S = []
			t = target
			if DBG:
				print previous
			while previous[t] is not None:
				if DBG:
					print t
				S.append(t)
				t = previous[t]
			S.append(source)
			return S
		
		if u[0] == INFTY:
			dist.put(u)
			break

		if DBG:
			print "Iterating through: ", Graph[u[1]]

		for v in Graph[u[1]]:
			alt = u[0] + dist_between(u[1], v) # distance of this node using the current path to get to it
			if alt < get_distance(v): # if this distance is more interesting that the previously stored one
				distances[v] = alt ;
				dist.put((alt, v)) # duplicate with the current (former_distance, v) stored there but priority queue => should not come out... before the end (and it avoids looking for a specific value in the queue)
				previous[v] = u[1] ;
	return distances;

print "G=", G
print Dijkstra(G, 0, 4);







