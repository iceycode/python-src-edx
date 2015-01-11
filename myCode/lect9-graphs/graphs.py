__author__ = 'Allen'
__doc__ = """some graph examples """

# Representation of permutations of students in line
# Nodes represent permutations of students in the line
# Edges connect 2 permutations if one can be made into the other by
#   swapping adjacent students, ONLY if they are next to each other
#   example: ABC & ACB but NOT ABC & CAB

#from graph import *
#Graph implementation in python

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return str(self.src) + '->' + str(self.dest)

#weight associated with source & destination
class WeightedEdge(Edge):
    def __init__(self, src, dest, weight = 3):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return str(self.src) + '->' + str(self.dest) + ' (' \
            + str(self.weight) + ')'


#1-directional graph
class Digraph(object):
    def __init__(self):
        self.nodes = set([]) #built-in python for collecting together objects
        self.edges = {}

    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []

    #creates adjacency list
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()

        # if src & dest not part of the graph
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.nodes

    #representation of graph
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d) + '\n'
        return res[:-1]


#bidirectional graph (extension of digraph)
class Graph(Digraph):
    '''
    adds reverse direction edge from digraph
    '''
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


def printPath(path):
    # a path is a list of nodes
    result = ''
    for i in range(len(path)):
        if i == len(path) - 1:
            result = result + str(path[i])
        else:
            result = result + str(path[i]) + '->'
    return result

# taken from problem 3 in lecture 9
def getNodes():
    nodes = []
    nodes.append(Node("ABC")) # nodes[0]
    nodes.append(Node("ACB")) # nodes[1]
    nodes.append(Node("BAC")) # nodes[2]
    nodes.append(Node("BCA")) # nodes[3]
    nodes.append(Node("CAB")) # nodes[4]
    nodes.append(Node("CBA")) # nodes[5]

    return nodes

def graphLinePermutations_Digraph():
    nodes = getNodes()

    dg = Digraph()
    for n in nodes:
        dg.addNode(n)

    add_edges(nodes, dg)

#returns a graph of line permutations
def graphLinePermutations():
    nodes = getNodes()

    g = Graph()
    for n in nodes:
        g.addNode(n)

    add_edges(nodes, g)

    printEdges(nodes, g)
    return g


# this simple solution by looking at permutations
def addEdgesSimple(nodes, g):
    g.addEdge(Edge(nodes[0], nodes[1]))
    g.addEdge(Edge(nodes[0], nodes[2]))
    g.addEdge(Edge(nodes[1], nodes[4]))
    g.addEdge(Edge(nodes[2], nodes[3]))
    g.addEdge(Edge(nodes[3], nodes[5]))
    g.addEdge(Edge(nodes[4], nodes[5]))

# this implementation checks for connections b/w nodes
#  adds edges to nodes if characters can be swapped to form
# ONLY THE ADJACENT set
# only b/w elements in the set beside each other
# s1 = n.getName()[1::-1] # reverse 1st 2 chars
# s2 = n.getName()[2:0:-1] # reverse last 2 chars
def add_edges(nodes, graph):
    for n in nodes:
        copy = nodes[:]
        s1 = n.getName()[0:2]
        s1r = s1[::-1] # reverse 1st 2 chars
        s2 = n.getName()[1:]
        s2r = s2[::-1] # reverse last 2 chars
        copy.remove(n) # so it does not compare itself
        findEdges(n, [s1r, s2r], copy, graph)

def findEdges(node, pairs, others, graph):
    for n in others:
        s1 = n.getName()[0:2]
        s2 = n.getName()[1:]
        if s1==pairs[0]:
            edge = Edge(node, n)
            if node not in graph.childrenOf(n):
                graph.addEdge(edge)
        elif s2==pairs[1]:
            edge = Edge(node, n)
            if node not in graph.childrenOf(n):
                graph.addEdge(edge)


def printEdges(nodes, g):

    for n in nodes:
        childNodes = g.childrenOf(n)
        print n.getName()
        for node in childNodes:
            print "-->", node.getName()

graphLinePermutations()