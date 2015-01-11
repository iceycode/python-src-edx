# 6.00.2x Problem Set 5
# Graph optimization
#
# A set of data structures to represent graphs
#

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)


class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}

    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            #raise ValueError('Duplicate node')
            pass
        else:
            self.nodes.add(node)
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        # if not(dest in self.edges[src]):
        self.edges[src].append(dest)

    def getEdges(self):
        return self.edges

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.nodes

    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]

# a graph of sites connected
class SiteGraph(Digraph):
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = []
        self.inEdges = []
        self.outEdges = []
        self.edges = {}
        self.allEdges = []

    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        # if not(dest in self.edges[src] and src in self.edges[src]):
        self.inEdges.append(src)
        self.outEdges.append(dest)
        self.edges[src].append(dest)

    def addInEdge(self, edge):
        if not (edge in self.nodes):
            raise ValueError('Node not in graph')
        self.inEdges.append(edge)

    def addOutEdge(self, edge):
        self.outEdges.append(edge)

    def meanShortestPath(self, src):
        meanShortestPath = []
        for k in self.edges:
            mean = sum(self.edges[k])/len(self.edges[k])

        return meanShortestPath

    def getEdges(self):
        return self.edges

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.nodes

    def allNodes(self):
        return self.nodes

    def allEdges(self):
        return self.edges

    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]



# weighted edge
class WeightedEdge(Edge):
    '''
    weight stores information about distance travelled
     weight can be distance travelled outside & total distance
    '''
    def __init__(self, src, dest, total, outside):
        Edge.__init__(self, src, dest)
        self.outdoor = outside
        self.total = total

    def getOutdoorDistance(self):
        return self.outdoor

    def getTotalDistance(self):
        return self.total

    def __str__(self):
        srcdest = Edge.__str__(self)
        dists = '{0} ({1}, {2})'.format(srcdest, self.total, self.outdoor)
        return dists


# Weighted digraph (unidirectional)
class WeightedDigraph(Digraph):

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        totalDist = edge.getTotalDistance()
        outdoorDist = edge.getOutdoorDistance()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append([dest, (totalDist, outdoorDist)])

    def childrenOf(self, node):
        children = []
        for n in self.edges[node]:
            children.append(n[0])
        return children

    def __str__(self):
        st = ''
        for k in self.edges:
            for d in self.edges[k]:
                d1, d2 = d[1]
                d1 = float(d1)
                d2 = float(d2)
                st += '{0}->{1} ({2}, {3})\n'.format(k.getName(), d[0].getName(), d1, d2)

        return st[:-1]