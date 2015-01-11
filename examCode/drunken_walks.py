__author__ = 'Allen'

import math
import random, pylab

class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

#-----COLLISIONS into VARYING walls-------
'''
1) SW (Solid walls): cannot go through fence, if drunk sees that his move will make him
        run into fence, drunk will hesitate & not move from the spot
2) SP (Small planet): rightmost edge is connected to leftmost edge & top edge to bottom
3) WW (Warped world): if drunk moves past right-most edge, ends up on the top edge & vice versa.
                if moves past left edge, ends up on bottom edge & vice versa
4) BH (back to home): whenever drunk reaches any edge, gets transpotrted back to center of world

'''
    # leftEdge = edges[0]
    # rightEdge = edges[1]
    # bottomEdge = edges[2]
    # topEdge = edges[3]
    # x = location.x
    # y = location.y

    # ought to be a Small Planet type fence...
    #  if implemented correctly
    # if x+dx > leftEdge and x+dx < rightEdge:
    #     x += dx
    # if  y+dy > bottomEdge and y+dy < topEdge:
    #     y += dy


    #probably will not work



    # if x+dx > leftEdge and x+dx < rightEdge:
    #     x += dx
    # elif x+dx > rightEdge:
    #     x = leftEdge + (x+dx - rightEdge)
    # elif x+dx < leftEdge:
    #     x = rightEdge - (leftEdge - (x+dx))
    #
    # if  y+dy > bottomEdge and y+dy < topEdge:
    #     y += dy
    # elif y+dy > topEdge:
    #     y = bottomEdge + (y+dy - topEdge)
    # elif y+dy < bottomEdge:
    #     y = topEdge - (bottomEdge - (y+dy))


# world class, like field, but contains fences
class EnclosedField(Field):
    def __init__(self):
        super(EnclosedField, self).__init__()
        self.fences = [] #like areas enclosed in graph




class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
            [(0.0,0.9), (0.0,-1.03), (1.03, 0.0), (-1.03, 0.0)]
        return random.choice(stepChoices)

class EDrunk(Drunk):
    def takeStep(self):
        ang = 2 * math.pi * random.random()
        length = 0.5 + 0.5 * random.random()
        return (length * math.sin(ang), length * math.cos(ang))

class PhotoDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.0, 0.5),(0.0, -0.5),
                     (1.5, 0.0),(-1.5, 0.0)]
        return random.choice(stepChoices)

class DDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.85, 0.85), (-0.85, -0.85),
                     (-0.56, 0.56), (0.56, -0.56)]
        return random.choice(stepChoices)







#new function for random walk calculation of actual x & y distance
def walkVector(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(f.getLoc(d).getX() - start.getX(),
           f.getLoc(d).getY() - start.getY())


def simWalks(numSteps, numTrials, dClass):
    homer = dClass('Homer')
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walkVector(f, homer, numSteps))
    return distances


def drunkTestP(numTrials = 100):
    stepsTaken = 1000
    for dClass in (UsualDrunk, ColdDrunk, EDrunk, PhotoDrunk, DDrunk):
        # meanXDistances = []
        # meanYDistances = []
        xAxis = []
        yAxis = []
        distances = simWalks(stepsTaken, numTrials, dClass)

        for i in xrange(numTrials):
            x, y = distances[i]
            xAxis.append(x)
            yAxis.append(y)
            # meanXDistances.append(sum(xAxis)/len(xAxis))
            # meanYDistances.append(sum(yAxis)/len(yAxis))
        pylab.xlim(-100, 100)
        pylab.ylim(-100, 100)
        pylab.plot(xAxis, yAxis, 'bo')
        pylab.title('Actual Distance from Origin for '+ dClass.__name__)
        pylab.xlabel('Steps Taken')
        pylab.ylabel('Steps from Origin')
        #pylab.legend(loc = 'upper left')
        pylab.figure()
    pylab.show()


drunkTestP()