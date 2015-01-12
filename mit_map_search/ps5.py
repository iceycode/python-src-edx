# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#  using Breadth-First and Directed Depth-First Search algorithms
# NOTE: changing the graph data structure, specifically how the weighted edges
#  are associated with nodes, would go a long way in helping with implementation

import string
# This imports everything from `graph.py` as if it was defined in this file!
from mit_map_search.graph import *



#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph. 
# Each location is a point on a directed graph
# In file, each int represents in order following, seperated by a space
#    start building     destination building     total distance     outdoors distance
#  Nodes: start & desintation buildings
#  Edges: src = start; dest = end building, total distance, outdoors distance
# Steps:
#       1: parse the file, using deliminter
#       2: create nodes with first 2 integers
#       3: create an edge using next 2 integers
#       4: add that edge to the graph
#       5: repeat untill end of list

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph
    Each entry in the map file consists of the following four positive
    integers, separated by a blank space:
        From To TotalDistance DistanceOutdoors
                e.g.   32 76 54 23 ---> an edge from 32 to 76.
    :param: name of the map file
    :return: a directed graph representing the map
    """
    print "Loading map from file..."
    #129 entries in mapFile
    try:
        mapFile = open(mapFilename, 'r', 0) #creates String list of lines
    except IOError as e : #line of code to be added here# OR except IOError : OR except IOError as e
        print "Entered wrong filename or it does not exist!"


    mitMap = WeightedDigraph() # the weighted digraph


    entries = [] # list of map entries (lines)
    while True:
        path = mapFile.readline()
        if not path:
            break
        else:
            entry = string.split(path, ' ')
            addToGraph(entry, mitMap)

    return mitMap


# adds lines (entries) from mapFile to graph
def addToGraph(entry, g):
     start = Node(entry[0])
     end = Node(entry[1])
     addNodeToGraph(start, g)
     addNodeToGraph(end, g)

     totalDist = int(entry[2])
     outdoorDist = int(entry[3])
     edge = WeightedEdge(start, end, totalDist, outdoorDist)
     addEdgeToGraph(edge, g)

def addNodeToGraph(node, g):
    try:
        g.addNode(node)
    except ValueError, e:
        print "Node already added; ", str(e)

def addEdgeToGraph(edge, g):
    try:
        g.addEdge(edge)
    except ValueError, e:
        print "No src or destination node in graph; ", str(e)


#
# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
#   and what the constraints are
#


'''
NOTE: inconsistent results b/w online grader, own calculations & tests
- this mainly has to do with the ridiculously vague directions
  on how nodes and edges are added to the graph
  - for example, grader shows that e[1] is a string, which my own tests do not show

Just like a DFS search
 - checks all possible nodes possible, continues to until finds#
PSEUDOCODE:
    1. generae destination nodes of start (childrenOf)
    2. check 1st destination node in path
    3. if start == end & constaints met, return paths; else, child nodes of curr node
    4. check next child of start and generate all childNodes, repeat 2
    5. if end reached & path doe not satisfy max constraints, raise ValueError


'''

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Assumes: start and end are numbers for existing buildings in graph
    path looks like: edges are dictionaries: {'src':[x,{d1,d2}]...'end':[x]}
    :param: digraph: instance of class Digraph or its subclass
    :param: start location
    :param: end location
    :param: maxTotalDist : maximum total distance on a path (integer)
    :param: maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    :returns: The shortest-path from start to end, represented by
            a list of building numbers (in strings), [n_1, n_2, ..., n_k],
            where there exists an edge from n_i to n_(i+1) in digraph,
            for all 1 <= i < k.

            If there exists no path that satisfies maxTotalDist and
            maxDistOutdoors constraints, then raises a ValueError.
    """
    shortestPath = [] # the shortest path

    # generates ALL paths from start to end
    # pathsInRange = findPathsInRangeBFS(digraph, Node(start), Node(end), maxDistOutdoors)
    pathsInRange = iterBFS(digraph, Node(start), Node(end), maxTotalDist, maxDistOutdoors)



    shortestDist = -1
    totalDistance = 0
    for i in xrange(len(pathsInRange)):
        n = pathsInRange[i]
        if n[0] == Node(start):
            totalDistance = 0
            candidatePath = []
        else:
            d1, d2 = n[1]
            totalDistance += d1
            if totalDistance <= maxTotalDist:
                candidatePath.append(n[0])
            if n[0] == Node(end):
                if shortestDist == -1:
                    shortestDist = totalDistance
                    shortestPath = candidatePath
                elif shortestDist > totalDistance:
                    shortestDist = totalDistance
                    shortestPath = candidatePath

    # just add start node to shortest path
    shortestPath.insert(0, Node(start))

    shortestPathAsString = []
    for n in shortestPath:
        shortestPathAsString.append(n.getName())

    return shortestPathAsString



# iterative brute force search helper function
def iterBFS(g, start, end, maxTotalDist, maxDistOutdoors, q = []):
    initPath = [[start, (0, 0)]]
    q = []
    q.append(initPath)
    while len(q) != 0:
        tempPath = q.pop(0) # pop off of queue
        lastNode = tempPath[len(tempPath)-1] # last node
        d1, d2 = lastNode[1] # get distances

        if lastNode[0] == end and d2 <= maxDistOutdoors: # and d1 <= maxTotalDist
            return tempPath

        # get the paths
        for e in g.edges[lastNode[0]]:
            ed1, ed2 = e[1]
            if e[0] not in [n[0] for n in tempPath]:
                if d2+ed2 <= maxDistOutdoors:
                    # d1+ed1 <= maxTotalDist and
                    newPath = tempPath + [[e[0], (d1+ed1, d2+ed2)]]
                    q.append(newPath)

    raise ValueError # node not there

#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors. Assumes:
        start and end are numbers for existing buildings in graph

    :param: digraph: instance of class Digraph or its subclass
    :param: start location
    :param: end location
    :param: maxTotalDist : maximum total distance on a path (integer)
    :param: maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    :return: The shortest-path from start to end, represented by
            a list of building numbers (in strings), [n_1, n_2, ..., n_k],
            where there exists an edge from n_i to n_(i+1) in digraph,
            for all 1 <= i < k.

            If there exists no path that satisfies maxTotalDist and
            maxDistOutdoors constraints, then raises a ValueError.
    """
    shortestPath = findPathsDirectedDFS(digraph, [Node(start)], Node(end),
                                        maxDistOutdoors, maxTotalDist)


    if Node(end) not in [e[0] for e in shortestPath]:
        raise ValueError

    spathstring = []
    for n in shortestPath:
        spathstring.append(n[0].getName())


    return spathstring






# helper functions for directedDFS
def findPathsDirectedDFS(g, start, end, maxOutdoorDist, maxTotalDist,
                         outdoor = 0.0, total = 0.0, shortestDist = 0.0,
                         path = [], spath = None, edgeChecked = []):
    path = path + [start]

    if start[0] == end:
        return path

    edges = g.edges[start[0]][:]
    for e in edges:
        d1, d2 = e[1]
        # if len(path) > 0:
        #     distances = [e[1] for n in path[1:]]
        #     for o in distances:
        #         tot, out = o
        #         outdoor += out
        #         total += tot
        outdoor += d2
        total += d1
        if outdoor <= maxOutdoorDist and total <= maxTotalDist:
            if e[0] not in [n[0] for n in path]:
                edgeChecked.append(e)
                if spath == None or total <= shortestDist:
                    newPath = findPathsDirectedDFS(g, e, end, maxOutdoorDist, maxTotalDist,
                                                   outdoor, total,
                                                   shortestDist, path, spath, edgeChecked)
                    if newPath != None:
                        shortestDist = total
                        spath = newPath
        else:
            outdoor -= d2
            total -= d1

    return spath


# iterative directed depth first force search helper function
def iterDirectedDFS(g, start, end, maxTotalDist, maxDistOutdoors, q = []):
    initPath = [[start, (0, 0)]]
    q = []
    q.append(initPath)
    while len(q) != 0:
        tempPath = q.pop(0) # pop off of queue
        lastNode = tempPath[len(tempPath)-1] # last node
        d1, d2 = lastNode[1] # get distances

        if lastNode[0] == end and d2 <= maxDistOutdoors: # and d1 <= maxTotalDist
            return tempPath

        # get the paths
        for e in g.edges[lastNode[0]]:
            ed1, ed2 = e[1]
            if e[0] not in [n[0] for n in tempPath]:
                if d2+ed2 <= maxDistOutdoors:
                    # d1+ed1 <= maxTotalDist and
                    newPath = tempPath + [[e[0], (d1+ed1, d2+ed2)]]
                    q.append(newPath)

    raise ValueError # node not there
