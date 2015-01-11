# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import * 



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
    pathsInRange = [] # list that keeps initial outdoor paths within range
    candidates = [] # list of paths based on total distance
    shortestPath = [] # the shortest path
    shortestDist = 0 # stores current shortest

    # generates ALL paths from start to end
    pathsInRange = findPathsInRange(digraph, Node(start) , Node(end), maxDistOutdoors)

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

    if Node(end) not in shortestPath:
        raise ValueError

    shortestPathAsString = []
    for n in shortestPath:
        shortestPathAsString.append(n.getName())

    return shortestPathAsString


# helper functions
# RECURSIVELY finds all paths in distance range
def findPathsInRange(g, start, end, maxDist, path = [], pathsInRange = []):
    '''
    Finds all the paths outside within range of max outside distance
    - same as a DFS algorithm, instead of shortest path, finds path within constraint
       of max outdoor distance

    :param g: the digraph
    :param start: the current start node
    :param end: the final destination
    :param maxDist: the constraint (either maxDistOutdoors or maxTotalDist
    :param distance: the current distance
    :param checkTotal:
    :returns: a new path to check (if it is end), paths in range or raises value error no end
    '''
    path = path + [start] # add current node to path (if start it is first

    if start[0] == end: # returns path if end is reached
        return path

    edges = g.edges[start[0]] # get edges

    # for node in g.childrenOf(path[len(path)-1][0]):
    for e in edges: # iterate through each edge
        # get distance
        d1, d2 = e[1]
        if len(path) > 1:
            prev1, prev2 = path[len(path)-1][1]
            distance = d2 + prev2
        else:
            distance = 0
        if e not in path and distance <= maxDist: # prevent cycling
            newPath = findPathsInRange(g, e, end, maxDist, path, pathsInRange)
            if len(newPath)>1:
                lastNode = newPath[len(newPath)-1][0]
                if end == lastNode:
                    pathsInRange = pathsInRange + newPath

    return pathsInRange

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


# helper functions for directedDFS ORIGINAL
# def findPathsDDFS(g, start, end, maxOutdoorDist, maxTotalDist, outdoor = 0.0, total = 0.0, shortestDist = 0, path = []
#                   , spath = None):
#     path = path + [start]
#
#     if start[0] == end:
#         return path
#
#     edges = g.edges[start[0]]
#     for e in edges:
#         d1, d2 = e[1]
#         outdoor += d2
#         total += d1
#         if outdoor <= maxOutdoorDist and total <= maxTotalDist:
#             if e[0] not in [n[0] for n in path]:
#                 if spath == None or total > shortestDist:
#                     newPath = (g, e[0], end, maxOutdoorDist, maxTotalDist, outdoor, total, shortestDist, path, spath)
#                     if newPath != None:
#                         spath = newPath
#         else:
#             outdoor -= d2
#             total -= d1
#
#     return spath
# Uncomment below when ready to test
#### NOTE! These tests may take a few minutes to run!! ####
# if __name__ == '__main__':
#     Test cases
#     mitMap = load_map("mit_map.txt")
#     print isinstance(mitMap, Digraph)
#     print isinstance(mitMap, WeightedDigraph)
#     print 'nodes', mitMap.nodes
#     print 'edges', mitMap.edges


#     LARGE_DIST = 1000000

#     Test case 1
#     print "---------------"
#     print "Test case 1:"
#     print "Find the shortest-path from Building 32 to 56"
#     expectedPath1 = ['32', '56']
#     brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
#     dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath1
#     print "Brute-force: ", brutePath1
#     print "DFS: ", dfsPath1
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

#     Test case 2
#     print "---------------"
#     print "Test case 2:"
#     print "Find the shortest-path from Building 32 to 56 without going outdoors"
#     expectedPath2 = ['32', '36', '26', '16', '56']
#     brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
#     dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
#     print "Expected: ", expectedPath2
#     print "Brute-force: ", brutePath2
#     print "DFS: ", dfsPath2
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)

#     Test case 3
#     print "---------------"
#     print "Test case 3:"
#     print "Find the shortest-path from Building 2 to 9"
#     expectedPath3 = ['2', '3', '7', '9']
#     brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#     dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath3
#     print "Brute-force: ", brutePath3
#     print "DFS: ", dfsPath3
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)

#     Test case 4
#     print "---------------"
#     print "Test case 4:"
#     print "Find the shortest-path from Building 2 to 9 without going outdoors"
#     expectedPath4 = ['2', '4', '10', '13', '9']
#     brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
#     dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
#     print "Expected: ", expectedPath4
#     print "Brute-force: ", brutePath4
#     print "DFS: ", dfsPath4
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)

#     Test case 5
#     print "---------------"
#     print "Test case 5:"
#     print "Find the shortest-path from Building 1 to 32"
#     expectedPath5 = ['1', '4', '12', '32']
#     brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#     dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
#     print "Expected: ", expectedPath5
#     print "Brute-force: ", brutePath5
#     print "DFS: ", dfsPath5
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)

#     Test case 6
#     print "---------------"
#     print "Test case 6:"
#     print "Find the shortest-path from Building 1 to 32 without going outdoors"
#     expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
#     brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
#     dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
#     print "Expected: ", expectedPath6
#     print "Brute-force: ", brutePath6
#     print "DFS: ", dfsPath6
#     print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)

#     Test case 7
#     print "---------------"
#     print "Test case 7:"
#     print "Find the shortest-path from Building 8 to 50 without going outdoors"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
    
#     try:
#         directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
    
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr

#     Test case 8
#     print "---------------"
#     print "Test case 8:"
#     print "Find the shortest-path from Building 10 to 32 without walking"
#     print "more than 100 meters in total"
#     bruteRaisedErr = 'No'
#     dfsRaisedErr = 'No'
#     try:
#         bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         bruteRaisedErr = 'Yes'
    
#     try:
#         directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
#     except ValueError:
#         dfsRaisedErr = 'Yes'
    
#     print "Expected: No such path! Should throw a value error."
#     print "Did brute force search raise an error?", bruteRaisedErr
#     print "Did DFS search raise an error?", dfsRaisedErr
