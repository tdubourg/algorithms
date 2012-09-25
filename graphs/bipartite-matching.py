#!/usr/bin/python

"""
Algorithm description: Implementing the Hopcroft-Karp algorithm for findin a maximum matching in a bipartite graph.
Input: Bipartite graph, represented with adjacence lists from the point of view of the "left" part of the bipartite graph
Ouput: The nodes matched (in Pair) and the cardinality of the matching

Author: TD
License: GPLv3
"""

import sys
from collections import deque

INFTY = float('inf')
Q = deque()
Dist = {}
Adj = {}
G = {}
G1 = {}
Pair = {}
Pair = {}

def Dequeue(Q):
    return Q.popleft()

def Enqueue(Q, v):
    return Q.append(v)
    
def Empty(Q):
    return (len(Q) == 0)

def BFS (): # breadth first search
    global G1, Pair, Pair, None, Q, Dist, Adj
    
    print "----- Entering BFS -----"

    for v in G1:
        if Pair[v] is None:
            print "Unpaired vertex:", v, "setting distance=0"
            Dist[v] = 0
            Enqueue(Q,v)
        else:
            print "Already paired vertex:", v, "setting distance=infty"
            Dist[v] = INFTY
    Dist[None] = INFTY

    while Empty(Q) == False:
        print "State of the queue:", Q
        v = Dequeue(Q)
        print "Unqueuing, current element=", v
        try:
            print "For each neighboor of", v, " (", G1[v], "):"
            for u in G1[v]:
                print "Current neighboor:", u
                print "Current neighboor paired with:", Pair[u]
                if Dist[ Pair[u] ] == INFTY:
                    print "Current neighboor dist is INFTY, update dist[] and Enqueue", u
                    Dist[ Pair[u] ] = Dist[v] + 1
                    Enqueue(Q, Pair[u])
        except KeyError:
            print ""
            pass
    return Dist[None] != INFTY

def DFS (v): # depth-first-search
    print "----- Entering DFS -----"
    global G1, Pair, Pair, None, Q, Dist, Adj
    if v != None:
        print "v != None"
        # for each node in the neighboors of v...
        print "For each neighboor of", v, " (", G1[v], "):"
        for u in G1[v]:
            print "Current neighboors=", u
            if Dist[ Pair[u] ] == Dist[v] + 1: # means they are neighboors
                print u, "has been paired with a vertex", Pair[u], "whose distance is near to the one of", v
                if DFS(Pair[u]) == True:
                    print "Either", u, "is not paired or ??"
                    print "Pairing",u, "with", v
                    Pair[u] = v
                    Pair[v] = u
                    print "Returning True because we just paired two elements (thus augmenting the matching)"
                    return True
        Dist[v] = INFTY
        return False
    else:
        print "v=None"
    return True

def Hopcroft_Karp(graph):
    global G1, Pair, Pair, None, Q, Dist, Adj
    
    Adj = graph
    G1 = G = graph
    Dist = {i:INFTY for i in xrange(0, len(graph)*2)}
    
    Pair = {i:None for i in xrange(0, len(graph)*2)}
    # Pair = {i:None for i in xrange(0, len(graph)*2)}
        
    matching = 0
    while BFS() == True:
        print "For each node of G1"
        for v in G1:
            if Pair[v] == None:
                print "Node", v, "is unpaired, trying to pair it"
                if DFS(v) == True:
                    print "Found a new element in the matching"
                    matching = matching + 1
            else:
                print "Node", v, "already paired"
    
    print "Pair",Pair
    print "Pair",Pair
    print "G",G
    print "G1",G1
    print "Adj",Adj
    print "Dist",Dist
    print "Matching", matching
    
    return matching, Pair

# g = {0: [4, 5], 1:[5,6], 2:[4], 3: [6,7]}
g = {0: [4, 5], 1:[5,6], 2:[4,7], 3: [6,7,4]}


print "Result:", Hopcroft_Karp(g);
