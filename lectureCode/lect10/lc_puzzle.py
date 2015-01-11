class puzzle(object):
    def __init__(self, order):
        self.label = order # id of tile
        for index in range(9):
            if order[index] == '0':
                self.spot = index # where it exists
                return None
    # generates tiles
    def transition(self, to):
        label = self.label #
        blankLocation = self.spot # the black spot
        newBlankLabel = str(label[to]) # what tile is going there
        newLabel = ''
        for i in range(9):
            if i == to:
                newLabel += '0' # blank in spot
            elif i == blankLocation:
                newLabel += newBlankLabel
            else:
                newLabel += str(label[i])
        return puzzle(newLabel)
    def __str__(self):
        return self.label



def DFSWithGeneratorShortest(start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    if start.label == end.label:
        return path
    for shift in shiftDict[start.spot]:
        new = start.transition(shift)
        if new.label not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                newPath = DFSWithGeneratorShortest(new,end,path,shortest)
                if newPath != None:
                    shortest = newPath
    return shortest

def BFSWithGenerator(start, end, q = []):
    initPath = [start]
    q.append(initPath) # put into q
    while len(q) != 0:
        tmpPath = q.pop(0) # takes 1st thing off q
        lastNode = tmpPath[len(tmpPath) - 1] # gives last point in sequence
        if lastNode.label == end.label:
            return tmpPath
        # figure out transitions by looking at last node
        for shift in shiftDict[lastNode.spot]:
            new = lastNode.transition(shift) # compute new state of system
            #check that node not in path
            if notInPath(new, tmpPath):
                newPath = tmpPath + [new] # create new path
                q.append(newPath) # explicitly put at end of queue
    return None

# uses stack to keep track of things
def DFSWithGenerator(start, end, stack = []):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    initPath = [start]
    stack.insert(0, initPath) # insert into 0
    while len(stack)!= 0:
        tmpPath = stack.pop(0)
        lastNode = tmpPath[len(tmpPath) - 1]
        if lastNode.label == end.label:
            return tmpPath
        for shift in shiftDict[lastNode.spot]:
            new = lastNode.transition(shift)
            if notInPath(new, tmpPath): #avoid cycles
                newPath = tmpPath + [new]
                stack.insert(0, newPath) # insert new path at top of queue
    return None

# whether node label is actually in the path
def notInPath(node, path):
    for elt in path:
        if node.label == elt.label:
            return False
    return True


shiftDict = {}
shiftDict[0] = [1, 3]
shiftDict[1] = [0, 2, 4]
shiftDict[2] = [1, 5]
shiftDict[3] = [0, 4, 6]
shiftDict[4] = [1, 3, 5, 7]
shiftDict[5] = [2, 4, 8]
shiftDict[6] = [3, 7]
shiftDict[7] = [4, 6, 8]
shiftDict[8] = [5, 7]

goal = puzzle('012345678')
test1 = puzzle('125638047')


def printGrid(pzl):
    data = pzl.label
    print data[0], data[1], data[2]
    print data[3], data[4], data[5]
    print data[6], data[7], data[8]
    print ''

def printSolution(path):
    for elt in path:
        printGrid(elt)

path = BFSWithGenerator(test1, goal) # gets sequence of moves
print printSolution(path) # prints out sequence path

path1 = DFSWithGenerator(test1, goal)




