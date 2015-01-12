__author__ = 'Allen'

'''TESTS
For WeightedGraph & Weighted Edge implementations
example of tests & output in IDLE
>>> g = WeightedDigraph()
>>> na = Node('a')
>>> nb = Node('b')
>>> nc = Node('c')
>>> g.addNode(na)
>>> g.addNode(nb)
>>> g.addNode(nc)
>>> e1 = WeightedEdge(na, nb, 15, 10)
>>> print e1
a->b (15, 10)
>>> print e1.getTotalDistance()
15
>>> print e1.getOutdoorDistance()
10
>>> e2 = WeightedEdge(na, nc, 14, 6)
>>> e3 = WeightedEdge(nb, nc, 3, 1)
>>> print e2
a->c (14, 6)
>>> print e3
b->c (3, 1)
>>> g.addEdge(e1)
>>> g.addEdge(e2)
>>> g.addEdge(e3)
>>> print g
a->b (15.0, 10.0)
a->c (14.0, 6.0)
b->c (3.0, 1.0)
'''

from mit_map_search.ps5 import *

def runTests1():
    g = WeightedDigraph()
    na = Node('a')
    nb = Node('b')
    nc = Node('c')
    g.addNode(na)
    g.addNode(nb)
    g.addNode(nc)
    e1 = WeightedEdge(na, nb, 15, 10)
    print e1 #a->b (15, 10)
    print e1.getTotalDistance() #15
    print e1.getOutdoorDistance() #10
    e2 = WeightedEdge(na, nc, 14, 6)
    e3 = WeightedEdge(nb, nc, 3, 1)
    print e2 # a->c (14, 6)
    print e3 # b->c (3, 1)
    g.addEdge(e1)
    g.addEdge(e2)
    g.addEdge(e3)
    print g #a->b (15.0, 10.0) \ a->c (14.0, 6.0) \b->c (3.0, 1.0)

def runTests2_findChildren():
    nh = Node('h')
    nj = Node('j')
    nk = Node('k')
    nm = Node('m')
    ng = Node('g')
    g = WeightedDigraph()
    g.addNode(nh)
    g.addNode(nj)
    g.addNode(nk)
    g.addNode(nm)
    g.addNode(ng)
    randomEdge = WeightedEdge(Node('j'), Node('h'), 94, 83)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(Node('j'), Node('k'), 100, 22)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(Node('h'), Node('k'), 10, 6)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(Node('h'), Node('j'), 18, 15)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(Node('h'), Node('k'), 63, 57)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(Node('m'), Node('k'), 12, 6)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(Node('m'), Node('j'), 10, 8)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(Node('m'), Node('k'), 10, 6)
    g.addEdge(randomEdge)
    print g.childrenOf(nh)#: [k, j, k]
    print g.childrenOf(nj)#: [h, k]
    print g.childrenOf(nk)#: []
    print g.childrenOf(nm)#: [k, j, k]
    print g.childrenOf(ng)#: []

def test_addToGraph1():
    print '\nAdding nodes & edges to weighted graph; test 1: '

    nx = Node('x')
    ny = Node('y')
    nz = Node('z')
    e1 = WeightedEdge(nx, ny, 18, 8)
    e2 = WeightedEdge(ny, nz, 20, 1)
    e3 = WeightedEdge(nz, nx, 7, 6)
    g = WeightedDigraph()
    g.addNode(nx)
    g.addNode(ny)
    g.addNode(nz)
    g.addEdge(e1)
    g.addEdge(e2)
    g.addEdge(e3)
    print g

    """
    CORRECT OUTPUT
    y->z (20.0, 1.0)
    x->y (18.0, 8.0)
    z->x (7.0, 6.0)
    """

def test_addEdges():
    print '\nAdding nodes & edges to weighted graph; test 2: '
    nj = Node('j')
    nk = Node('k')
    nm = Node('m')
    ng = Node('g')
    g = WeightedDigraph()
    g.addNode(nj)
    g.addNode(nk)
    g.addNode(nm)
    g.addNode(ng)
    m = Node('m')
    g1 = Node('g')
    j = Node('j')
    k = Node('k')

    randomEdge = WeightedEdge(m, g1, 12, 8)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(j, g1, 43, 39)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(m, k, 77, 33)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(j, k, 55, 52)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(m, g1, 44, 7)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(m, k, 30, 19)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(j, k, 99, 94)
    g.addEdge(randomEdge)
    randomEdge = WeightedEdge(k, g1, 45, 26)
    g.addEdge(randomEdge)
    print g
    """
    CORRECT OUTPUT:
    k->g (45.0, 26.0)
    j->g (43.0, 39.0)
    j->k (55.0, 52.0)
    j->k (99.0, 94.0)
    m->g (12.0, 8.0)
    m->k (77.0, 33.0)
    m->g (44.0, 7.0)
    m->k (30.0, 19.0)
    """


#runTests1()
#runTests2_findChildren()

# test_addToGraph1()
# test_addEdges()





# for loading the map
'''
>>> mitMap = load_map("mit_map.txt")
>>> print isinstance(mitMap, Digraph)

&&

>>> print isinstance(mitMap, WeightedDigraph)
'''

def test_Map():
    mitMap = load_map("mit_map.txt")

    print isinstance(mitMap, Digraph)
    print isinstance(mitMap, WeightedDigraph)

    nodes = mitMap.nodes
    print 'nodes = ', nodes

    edges = mitMap.edges
    print 'edges = ', edges

    print '\nPrint the mitMap as graph\n', mitMap

# test_Map()


def test_Searches():
    #Test cases
    mitMap = load_map("mit_map.txt")
    #print isinstance(mitMap, Digraph)
    #print isinstance(mitMap, WeightedDigraph)
    #print 'nodes', mitMap.nodes
    #print 'edges', mitMap.edges

    LARGE_DIST = 1000000

    #Test case 1
    print "---------------"
    print "Test case 1:"
    print "Find the shortest-path from Building 32 to 56"
    expectedPath1 = ['32', '56']
    brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath1
    print "Brute-force: ", brutePath1
    print "DFS: ", dfsPath1
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

    # Test case 2
    print "---------------"
    print "Test case 2:"
    print "Find the shortest-path from Building 32 to 56 without going outdoors"
    expectedPath2 = ['32', '36', '26', '16', '56']
    brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
    dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
    print "Expected: ", expectedPath2
    print "Brute-force: ", brutePath2
    print "DFS: ", dfsPath2
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)

    # #Test case 3
    print "---------------"
    print "Test case 3:"
    print "Find the shortest-path from Building 2 to 9"
    expectedPath3 = ['2', '3', '7', '9']
    brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
    dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath3
    print "Brute-force: ", brutePath3
    print "DFS: ", dfsPath3
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)
    #
    # #Test case 4
    # print "---------------"
    print "Test case 4:"
    print "Find the shortest-path from Building 2 to 9 without going outdoors"
    expectedPath4 = ['2', '4', '10', '13', '9']
    brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
    dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
    print "Expected: ", expectedPath4
    print "Brute-force: ", brutePath4
    print "DFS: ", dfsPath4
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)
    # #
    # # #Test case 5
    print "---------------"
    print "Test case 5:"
    print "Find the shortest-path from Building 1 to 32"
    expectedPath5 = ['1', '4', '12', '32']
    brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath5
    print "Brute-force: ", brutePath5
    print "DFS: ", dfsPath5
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)
    #
    # # #Test case 6
    print "---------------"
    print "Test case 6:"
    print "Find the shortest-path from Building 1 to 32 without going outdoors"
    expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
    brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
    dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
    print "Expected: ", expectedPath6
    print "Brute-force: ", brutePath6
    print "DFS: ", dfsPath6
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)
    #
    # # #Test case 7
    print "---------------"
    print "Test case 7:"
    print "Find the shortest-path from Building 8 to 50 without going outdoors"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
    except ValueError:
        bruteRaisedErr = 'Yes'

    try:
        directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
    except ValueError:
        dfsRaisedErr = 'Yes'

    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr
    #
    # # #Test case 8
    print "---------------"
    print "Test case 8:"
    print "Find the shortest-path from Building 10 to 32 without walking"
    print "more than 100 meters in total"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
    except ValueError:
        bruteRaisedErr = 'Yes'

    try:
        directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
    except ValueError:
        dfsRaisedErr = 'Yes'

    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr

test_Searches()