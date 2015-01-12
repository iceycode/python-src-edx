__author__ = 'Allen'
# code for final exam

import random

import pylab
from matplotlib.font_manager import FontProperties


# plots bimodal distribution
# a distribution is bimodal if made up of 2 normal distributions
#  with equal std deviations & means of each distribution seperated by
#   at least 2 std deviations
def bimodalDist():
    # gause(mu, sigma), mu = mean; sigma = std dev
    # will calling random.gauss, as seen in for loop, produce bimodal distribution?
    vals = [] # combined distributions (should make bimodal)
    vals1 = [] # 1st normal distribution
    vals2 = [] # second normal distribution
    for i in range(10):
        vals1.append(random.gauss(50,10))
        vals2.append(random.gauss(70,10))
        vals.append(vals1[i] + vals2[i])

    #pylab.title('Random Bimodal Distributions ')
    pylab.plot(vals1, 'b', label = 'Mean = 50')
    pylab.plot(vals2, 'g', label = 'Mean = 70')

    pylab.plot(vals, 'r', label = 'Bimodal')
    pFont = FontProperties()
    pFont.set_size('small')
    pylab.legend(loc=9, bbox_to_anchor =(0.7, -.01), ncol=3)
    pylab.show()

#bimodalDist()

def pylabPrint():
    a = 1.0
    b = 2.0
    c = 4.0
    yVals = []
    xVals = range(-20, 20)
    for x in xVals:
        yVals.append(a*x**2 + b*x + c)
    yVals = 2*pylab.array(yVals)
    xVals = pylab.array(xVals)
    try:
        a, b, c, d = pylab.polyfit(xVals, yVals, 3)
        print a, b, c, d
    except:
        print 'fell to here'


#pylabPrint()


def possible_mean(L):
    return sum(L)/len(L)

def possible_variance(L):
    mu = possible_mean(L)
    temp = 0
    for e in L:
        temp += (e-mu)**2
    return temp / len(L)

def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def variance(set, mean):
    var = 0.0
    for x in set:
        var += (x - mean)**2
    return var

def setCombos():
    allSets = []
    setA = [0,1,2,3,4,5,6,7,8]
    setB = [5,10,10,10,15]
    setC = [0,1,2,4,6,8]
    setD = [6,7,11,12,13,15]
    setE = [9,0,0,3,3,3,6,6]

    allSets.append(setA)
    allSets.append(setB)
    allSets.append(setC)
    allSets.append(setD)
    allSets.append(setE)

    i = 0
    setsAlike = []
    for set1 in allSets:
        i += 1
        print 'Set ' + str(i) + ' mean & var compared to others is: '
        print 'Set = ', set1
        for set2 in allSets :

            mean1 = sum(set1)/len(set1)
            var1 = variance(set1, mean1)
            mean2 = sum(set2)/len(set2)
            var2 = variance(set2, mean2)
            pVar1 = possible_variance(set1)
            pVar2 = possible_variance(set2)

            if set1 != set2:
                # if mean1 == mean2 and var1 == var2:
                if pVar1 == pVar2 and set1 not in setsAlike:
                    setsAlike.append(set1)
                    setsAlike.append(set2)

                print 'Means: ', mean1, ', ', mean2, ' Variances: ', var1, ', ', var2
                print 'possible variances: ', pVar1, ', ', pVar2

    if len(setsAlike)> 0:
        print 'Two sets are alike! They are: '
        for set in setsAlike:
            print set
    else:
        print 'no two sets have same mean, same variance OR same possible variance'

#setCombos()

def test_drunkMoves():
    rightEdge = 9
    leftEdge = 2
    topEdge = 9
    bottomEdge = 2

    x = 7
    y = 7
    dx = 3
    dy = -8
    # if x+dx < rightEdge and x+dx > leftEdge and y+dy < topEdge and y+dy > bottomEdge:
    #     x += dx
    #     y += dy
    # else:
    #     x = leftEdge + (rightEdge-leftEdge)/2
    #     y = bottomEdge + (topEdge-bottomEdge)/2

    # THIS IS UTTER NONSENSE since x,y cannot equal an int
    # if x+dx > rightEdge:
    #     x,y = (rightEdge-leftEdge)/2
    # if x+dx < leftEdge:
    #     x,y = (rightEdge-leftEdge)/2
    # if x+dx < rightEdge and x+dx > leftEdge:
    #     x += dx
    # if y+dy > topEdge:
    #     x,y = (rightEdge-leftEdge)/2
    # if y+dy < bottomEdge:
    #     x,y = (rightEdge-leftEdge)/2
    # if y+dy < topEdge and  y+dy > bottomEdge:
    #     y += dy


    if x+dx > rightEdge:
        x = y
    if x+dx < leftEdge:
        x = y
    if x+dx < rightEdge and x+dx > leftEdge:
        x += dx
    if y+dy > topEdge:
        y = x
    if y+dy < bottomEdge:
        y = x
    if y+dy < topEdge and  y+dy > bottomEdge:
        y += dy

    #
    # if x+dx < rightEdge and x+dx > leftEdge:
    #     x += dx
    # elif x+dx > rightEdge:
    #     x = bottomEdge
    # elif x+dx < leftEdge:
    #     x = topEdge
    # if y+dy < topEdge and  y+dy > bottomEdge:
    #     y += dy
    # elif y+dy > topEdge:
    #     y = leftEdge
    # elif y+dy < bottomEdge:
    #     y = rightEdge

    # # goes around like a planet (Small Planet Fence)
    # if x+dx < rightEdge and x+dx > leftEdge:
    #     x += dx
    # elif x+dx > rightEdge:
    #     x = bottomEdge
    # elif x+dx < leftEdge:
    #     x = topEdge
    # if y+dy < topEdge and  y+dy > bottomEdge:
    #     y += dy
    # elif y+dy > topEdge:
    #     y = leftEdge
    # elif y+dy < bottomEdge:
    #     y = rightEdge
    #


    return x, y

#print test_drunkMoves()



'''
Graphs: Problem 5
 representing internet has site x, linked to site y
Have a random graph, adds edges in non-uniform way.
 Initially no edges, n nodes
 Add edges in following way:
    choose Random node x
    choose node y with probability proportional to popularity or
        connectedness of y (ie, node with k edges 2x chosen than 2/k edge node

Each node has a set of incoming edges and a set of outgoing edges.
Each node has an in-degree: the number of incoming edges to the node AND
                out-degree: the number of outgoing edges from the node.
An edge cannot connect a node to itself &
    there can be at most one edge from a given x to a given y.

'''
from inclass_code.my_code.examCode.graph import *

def create_nodes(n):
    nodes = []
    for i in range(n):
        nodes.append(Node(i)) # newNode takes one parameter, the number of the node
    return nodes

def create_graph1(nodes):
    g = Digraph()
    for n in nodes:
        g.addNode(n)

    length = len(nodes)
    for i in xrange(len(nodes)):
        x = random.choice(nodes)
        y = random.choice(nodes)
        try:
            g.addEdge(Edge(x, y))
        except ValueError, e:
            length += 1
            print e.message

    graph_repr(g)

def create_graph2(nodes):
    g = Digraph()

    for n in nodes:
        g.addNode(n)

    for i in range(len(nodes)):
        x = random.choice(nodes)
        y = random.choice(nodes)
        try:
            g.addEdge(Edge(x,y))
            g.addEdge(Edge(y,x))
        except ValueError, e:
            print e.message

    graph_repr(g)

def create_graph3(nodes):
    g = Digraph()

    for n in nodes:
        g.addNode(n)

    length = len(nodes)
    for i in range(len(nodes)):
        w = random.choice(nodes)
        x = random.choice(nodes)
        y = random.choice(nodes)
        z = random.choice(nodes)
        try:
            g.addEdge(Edge(w,x))
            g.addEdge(Edge(x,y))
            g.addEdge(Edge(y,z))
            g.addEdge(Edge(z,w))
        except Exception, e:
            length += 1
            print e.message

    graph_repr(g)

def create_graph4(nodes):
    g = Digraph()

    for n in nodes:
        g.addNode(n)

    for x in nodes:
        for y in nodes:
            try:
                g.addEdge(Edge(x,y))
                g.addEdge(Edge(y,x))
            except ValueError, e:
                print e.message
    graph_repr(g)

def graph_repr(g):
    srcs = []
    for k in g.edges:
        srcs.append(k)
    srcs.sort()
    for k in srcs:
        dests = g.edges[k]
        dests.sort()
        print str(k), '--> ', dests


def test_graphTypes(n):
    nodes = create_nodes(n)
    print ' graph 1'
    create_graph1(nodes)
    print '\n graph 2'
    create_graph2(nodes)
    print '\n graph 3'
    create_graph3(nodes)
    print '\n graph 4'
    create_graph4(nodes)

test_graphTypes(5)




def initializeGraph(n): # n is an integer, the number of nodes in the graph
    G = SiteGraph() # Initializes an empty graph, with G.graphNodes set to []
    for i in range(n):
        G.addNode(Node(i)) # Node takes one parameter, the number of the node
    for i in range(n): #
    	x = G.nodes[i]
        y = G.nodes[(i+1) % n]
        G.addInEdge(x)
        G.addOutEdge(y)
        G.allEdges((x, y))

    return G


def randomPowerGraph(n):
    maxDegrees, meanDegrees, meanDegreeVariances, meanShortestPaths = [],[],[],[]
    graph = initializeGraph(n)
    for nEdges in range(n, n*n, n*n/10):
        graph.addEdges(nEdges)
        maxDegrees.append(graph.maxDegree())
        meanDegrees.append(graph.meanDegree())
        meanDegreeVariances.append(graph.meanDegreeVariances())
        meanShortestPaths.append(graph.meanShortestPath())

    pylab.title('Max Degrees Plot')
    pylab.figure(1)
    pylab.plot(maxDegrees, 'b')
    pylab.title('Mean Degrees Plot')
    pylab.figure(2)
    pylab.plot(meanDegrees, 'r')
    pylab.title('Mean Degree Variances Plot')
    pylab.figure(3)
    pylab.plot(meanDegreeVariances)
    pylab.title('Mean ShortestPaths Plot')
    pylab.figure(4)
    pylab.plot(meanShortestPaths)
    pylab.show()

#print '\nSiteGraph edges : ', initializeGraph(10)


randomPowerGraph(100)
