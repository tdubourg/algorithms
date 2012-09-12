#!/usr/bin/python

import Queue

dist = Queue.PriorityQueue()

INFTY = float('inf')

G = {
	0: {1: 30, 2: 30, 3: 10},
	1: {0: 30},
	2: {0: 30, 3: 5, 4: 9, 5:1},
	3: {2: 5, 4: 80, 0: 10, 5: 10},
	5: {2: 1, 4:1, 3:10},
	4: {3: 80, 2: 9, 5:23}
}

def Dijkstra(Graph, source, target):
	global INFTY
	previous = {}
	distances = {}

	def dist_between(u, v):
		# print "Asking dist(",u,",",v,")"
		return Graph[u][v]
		
	def _distances(u):
		try:
			return distances[u]
		except KeyError:
			return INFTY
	
	
	for v in Graph: 
	   	if v != source:
			distances[v] = INFTY
			dist.put((INFTY, v))
		previous[v] = None
		
	dist.put((0, source));
	distances[source] = 0
 	while not dist.empty():
		u = dist.get()
		print "Current u=",u
		if u[1] == target:
			print "Found!"
			S = []
			t = target
			print previous
			while previous[t] is not None:
				print t
				S.append(t)
				t = previous[t]
			S.append(source)
			return S
		
		if u[0] == INFTY:
			dist.put(u)
			break


	  	# deja fait via pop() remove u from Q ;
		print "Iterating through: ", Graph[u[1]]
		for v in Graph[u[1]]:
			alt = u[0] + dist_between(u[1], v)
			if alt < _distances(v):
				distances[v] = alt ;
				dist.put((alt, v)) # doublon mais priority queue donc on devrait pas le retrouver...avant la fin
				previous[v] = u[1] ;
	return distances;


print Dijkstra(G, 0, 4);







