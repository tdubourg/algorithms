#!/usr/bin/python

class Node:
	color= None
	key= None
	colorNames = {None: "NO COLOR", 1: "White", 2: "Black", 3: "Red", 4: "Green", 5: "Blue"}

	def __init__(self, k):
		self.key = k

	def __str__(self):
		return "(key=" + str(self.key) + ", color=" + str(Node.colorNames[self.color]) + ")"
	def __repr__(self):
		return self.__str__()

class Graph:
	edges= set()
	nodes= []
	nodesFromKeys = {}
	graph= {}
	
	colors = set([1, 2, 3, 4, 5, 6])
	_dbg = False

	def __init__(self):
		pass

	def addNode(self, node):
		self.nodes.append(node)
		self.nodesFromKeys[node.key] = node
		self.graph[node.key] = set()

	def addUndirectedEdge(self, N1, N2):
		try:
			self.graph[N1.key].add(N2)
		except:
			self.graph[N1.key] = set([N2])
		try:
			self.graph[N2.key].add(N1)
		except:
			self.graph[N2.key] = set([N1])

	def __str__(self):
		return str(self.graph)

	def fromInput(self):
		n = int(raw_input())

		for i in xrange(0, n):
			key = raw_input().strip()
			N = Node(key)
			self.addNode(N)

		while True:
			try:
				key1, key2 = raw_input().strip().split(" ")
				self.addUndirectedEdge(self.nodesFromKeys[key1], self.nodesFromKeys[key2])
			except EOFError:
				break

	def color(self):
		if self._dbg:
			print "self.nodes=", self.nodes

		while len(self.nodes) != 0:
			self.nodes = sorted(self.nodes, key=self.getdegree)
			node = self.nodes.pop()
			color = self.findSmallestNotInNeighboors(node)
			if self._dbg:
				print "Chosen color for", node, "is", Node.colorNames[color]
			node.color = color
		return self.nodesFromKeys.values()

	def findSmallestNotInNeighboors(self, node):
		c = set(self.colors)
		for n in self.graph[node.key]:
			if self._dbg:
				print "Neighboor:", n
				print "Colors:", c
			if n.color is not None:
				try:
					c.remove(n.color)
				except KeyError:
					pass # The color has already been taken out ? Just don't care
		if self._dbg:
			print c, len(c)
		if 0 == len(c):
			return None
		return c.pop()

	def getdegree(self, node):
		key = node.key
		if self._dbg:
			print "Getting the degree of node", key
			print "The degree is", len(self.graph[key])
		return len(self.graph[key])


if __name__ == '__main__':
	G = Graph()
	G.fromInput()
	# N1 = Node("Bla")
	# N2 = Node("Blo")
	# N3 = Node("Arg")
	# N4 = Node("Rok")
	# N5 = Node("Jajar")
	# G.addNode(N1)
	# G.addNode(N2)
	# G.addNode(N3)
	# G.addNode(N4)
	# # G.addNode(N5)
	# G.addUndirectedEdge(N1, N2)
	# G.addUndirectedEdge(N3, N2)
	# G.addUndirectedEdge(N1, N3)
	# G.addUndirectedEdge(N1, N4)
	print G.color()
