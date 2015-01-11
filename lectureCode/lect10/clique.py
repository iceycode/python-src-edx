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

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight = 1.0):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return str(self.src) + '->(' + str(self.weight) + ')'\
            + str(self.dest)

class Digraph(object):
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d) + '\n'
        return res[:-1]

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


def powerGraph(gr):
    nodes = gr.nodes
    nodesList = []
    for elt in nodes:
        nodesList.append(elt)
    pSet = powerSet(nodesList) # list of lists
    return pSet

def powerSet(elts):
    if len(elts) == 0:
        return [[]] # return element empty list if 0
    else:
        # 2 ^ (n-1) elements
        smaller = powerSet(elts[1:]) # all elements except 1st one
        elt = [elts[0]] # 1st element
        withElt = []
        for s in smaller:
            withElt.append(s + elt) # copy of list
        allofthem = smaller + withElt
        return allofthem


# finds the max clique of a graph
def maxClique(gr):
    candidates = powerGraph(gr) # all subgraphs of graph
    keepEm = []

    #go through all, & figure out if subgraph connected
    for candidate in candidates:
        if allConnected(gr, candidate):
            keepEm.append(candidate) # add to keepEm
    bestLength = 0
    bestSoln = None
    for test in keepEm:
        if len(test) > bestLength:
            bestLength = len(test)
            bestSoln = test
    return bestSoln


# checks completeness
def allConnected(gr,candidate):
    for n in candidate:
        for m in candidate:
            if not n == m:
                # check to make sure n is not child of m
                # if False, there is no edge, so false
                if n not in gr.childrenOf(m):
                    return False
    return True


def testGraph():
    nodes = []
    for name in range(5):
        nodes.append(Node(str(name)))
    g = Graph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[0]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[4],nodes[3]))
    return g


trialGraph = testGraph()
myClique = maxClique(trialGraph)
for n in myClique:
    print n.getName()


# testSet = [1, 2, 3, 4]
# ps = powerSet(testSet)
# print ps
        


