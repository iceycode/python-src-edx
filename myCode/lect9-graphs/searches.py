__author__ = 'Allen'
__doc__ = """ some practice with DFS & BFS pathfinding"""

#from graph import *
from graphs import *

def DFS(graph, start, end, path = []):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    print 'Current dfs path:', printPath(path)
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            newPath = DFS(graph,node,end,path,shortest)
            if newPath != None:
                return newPath


def DFSShortest(graph, start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    print 'Current dfs path:', printPath(path)
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path)<len(shortest):
                newPath = DFSShortest(graph,node,end,path,shortest)
                if newPath != None:
                    shortest = newPath
    return shortest




# find 1st path found from source to destination nodes
def testRandPoints(randSrc, randDest):
    paths = findAllPaths()
    sp = DFS(randSrc, randDest)
    len(sp)


def findAllPaths():
    nodes = getNodes()
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    add_edges(nodes, g)

    paths = []
    for src in nodes:
        for dest in nodes:
            paths.append(DFS(src, dest))

    return paths

def probShortestPath():
    paths = findAllPaths()
    nodes = getNodes()

    src = nodes[1]
    src = nodes[2]



probShortestPath()