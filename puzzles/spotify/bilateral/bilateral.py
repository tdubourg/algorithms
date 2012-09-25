#!/usr/bin/python

"""
Author: TD
License: GPLv3
"""

import sys
from copy import copy
from collections import deque


DBG = False


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
    Dist = {i:INFTY for i in graph}
    Pair = {i:None for i in graph}
        
    matching = 0
    # ---- END Init ----

    while BFS() == True:
        for v in G1:
            if Pair[v] == None:
                if DFS(v) == True:
                    matching = matching + 1
    
    # print "Pair",Pair
    # print "G1",G1
    # print "Dist",Dist
    # print "Matching", matching

    for (k,v) in Pair.items():
        if v is None:
            del Pair[k]
    
    return Pair

class Problem:
    _DBG = False
    graph = {}
    edgesSet = set()

    # Konig's theorem implementation, straight fron Wikipedia, once more
    def Konig(self, maxMatching):
        res = set()
        maxMatchingItems = maxMatching.items()
        Em = set(maxMatchingItems)

        if self._DBG:
            print     "Em=", Em
        
        E0 = self.edgesSet - Em
        
        if self._DBG:
            print "----------------"
            print "unmatched edges E0=", E0
            print "----------------"
        
        L, R = [set(_) for _ in zip(*self.edgesSet)]

        if self._DBG:
            print     "L, R=", L, ",", R
        
        matchedFromL, matchedFromR = [set(_) for _ in zip(*maxMatchingItems)]
        
        if self._DBG:
            print "matchedFromL, matchedFromR=", matchedFromL, matchedFromR

        UnmatchedVertFromL = L - matchedFromL
        UnmatchedVertFromR = R - matchedFromR
        if self._DBG:
            print     "UnmatchedVertFromL, UnmatchedVertFromR=", UnmatchedVertFromL, ",", UnmatchedVertFromR
        

        # Adding vertices unmatched from L
        T = UnmatchedVertFromL

        # The edges that are in those sets are not necessarily "bijective" (that's why we reconstruct them instead of trying to reuse any of )
        # Moreover, we need an "indexed" way to access them, a bunch of tuple would be incredibly slow
        rightFromLeft = {}
        for k,v in E0:
            try:
                rightFromLeft[k].add(v)
            except KeyError:
                rightFromLeft[k] = set([v])
            try:
                rightFromLeft[v].add(k)
            except KeyError:
                rightFromLeft[v] = set([k])
        
        leftFromRight = {}
        for k,v in maxMatchingItems:
            try:
                leftFromRight[k].add(v)
            except KeyError:
                leftFromRight[k] = set([v])
            try:
                leftFromRight[v].add(k)
            except KeyError:
                leftFromRight[v] = set([k])
        
        if self._DBG:
            print "----------------"
            print Em
            print leftFromRight
            print rightFromLeft
            print "----------------"
                
        # Adding vertices that are on alternating paths between E0 and Em starting at a vertex in UnmatchedVertFromL
        nextLeftVertices = T

        changed = True
        l = len(T)
        while changed: # As long as we have next elements to see (note: if nextLeftVertices is empty first, it will provoke nextRightVertices to be empty just after)
            # Adding the vertices "Reachable fron UnmatchedVertFromL by going l-t-r along edges from E0 and r-t-l from Em"
            nextRightVertices = set()
            for x in nextLeftVertices:
                try:
                    nextRightVertices |= rightFromLeft[x]
                except KeyError:
                    pass # No next vertex for this one, well, just don't do anything for it then

            nextLeftVertices = set()
            for x in nextRightVertices:
                try:
                    nextLeftVertices |= leftFromRight[x]
                except KeyError:
                    pass # No next vertex for this one, well, just don't do anything for it then

            T |= (nextLeftVertices | nextRightVertices)
            newL = len(T)
            if newL != l:
                changed = True
            else:
                changed = False
            l = newL

        
        if self._DBG:
            print "L, T, R="
            print L
            print T
            print R
            
        res = (L - T) | (R & T)
        return len(res), res

    def solve(self):
        # Get the max matching by Hopcroft-Karp
        maxMatching = Hopcroft_Karp(self.graph)

        if self._DBG:
            print "\n\nHopcroft_Karp():", maxMatching, "\n\n"

        # Transform it using Konig's theorem and solve it
        return self.Konig(maxMatching)

    def __init__(self, N, lines):
        for l in lines:

            if self._DBG:
                print "Current line: ", l

            ids = [int(_) for _ in l.strip().split(" ")]

            self.edgesSet.add((ids[0], ids[1]))
            try:
                self.graph[ids[0]].add(ids[1])
            except KeyError:
                self.graph[ids[0]] = set([ids[1]])

            try:
                self.graph[ids[1]].add(ids[0])
            except KeyError:
                self.graph[ids[1]] = set([ids[0]])

        if self._DBG:
            print "Graph:", self.graph
            print "Edges graph set:", self.edgesSet



if __name__ == "__main__":
    N = int(raw_input())
    lines = []
    while True:
        try:
            lines.append(raw_input())
        except EOFError:
            break

    # Prepare the problem
    pb = Problem(N, lines)
    # Solve it
    n, result = pb.solve()

    # Show off the solution to the Judges
    print n
    for e in result:
        print e 