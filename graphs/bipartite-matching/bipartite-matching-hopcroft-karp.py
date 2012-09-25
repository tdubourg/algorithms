
"""
Author: TD
License: GPLv3
"""

import sys
from collections import deque

INFTY = float('inf')
Q = deque()
Dist = {}
G1 = {}
Pair = {}

def Dequeue(Q):
    return Q.popleft()

def Enqueue(Q, v):
    return Q.append(v)
    
def Empty(Q):
    return (len(Q) == 0)

def BFS (): # breadth first search
    global G1, Pair, Q, Dist
    for v in G1: # for every node in the graph
        if Pair[v] is None: # if this node has not been matched yet
            Dist[v] = 0 # then the distance to this node is 0 (neighboor)
            Enqueue(Q,v) # and we put it in the queue
        else:
            Dist[v] = INFTY # else, if the node is already matched, consider it as never neighboor (infty distance from us)
    
    Dist[None] = INFTY
    # Goes through the queue elements
    while not Empty(Q): # As long as the queue is not empty
        v = Dequeue(Q)
        try:
            # For each neighboor of v (the element at the top of the queue)
            for u in G1[v]:
                if Dist[ Pair[u] ] == INFTY: # If the element paired with this neighboor is at infinity
                    Dist[ Pair[u] ] = Dist[v] + 1 # Then update this element's distance to current + 1
                    Enqueue(Q, Pair[u]) # Enqueue the paired element
        except KeyError:
            pass
    return Dist[None] != INFTY

def DFS (v): # depth-first-search
    global G1, Pair, Q, Dist
    if v != None:
        # for each node in the neighboors of v...
        for u in G1[v]:
            if Dist[ Pair[u] ] == Dist[v] + 1:
                if DFS(Pair[u]) == True:
                    Pair[u] = v
                    Pair[v] = u
                    return True
        Dist[v] = INFTY
        return False
    return True

def Hopcroft_Karp(graph):
    global G1, Pair, Pair, Q, Dist
    
    # ---- BEGIN Init ----
    G1 = graph
    Dist = {i:INFTY for i in xrange(0, len(graph)*2)}
    Pair = {i:None for i in xrange(0, len(graph)*2)}
        
    matching = 0
    # ---- END Init ----

    while BFS() == True:
        for v in G1:
            if Pair[v] == None:
                if DFS(v) == True:
                    matching = matching + 1
    
    print "Pair",Pair
    print "G1",G1
    print "Dist",Dist
    print "Matching", matching
    
    return matching

g = {0: [4, 5], 1:[5,6], 2:[4,7], 3: [6,7,4]}


print "Result:", Hopcroft_Karp(g);
