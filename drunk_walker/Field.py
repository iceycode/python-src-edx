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
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.__hash__()

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'



class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            drunk.setLocation(loc.x, loc.y)
            drunk.setDirection((loc.x, loc.y))
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

    def getDrunks(self):
        return self.drunks

    def getDrunkPosition(self, drunk):
        currLocation = self.drunks[drunk]
        return currLocation

#-----COLLISIONS into VARYING walls-------
'''
1) SW (Solid walls): cannot go through fence, if drunk sees that his move will make him
        run into fence, drunk will hesitate & not move from the spot
2) SP (Small planet): rightmost edge is connected to leftmost edge & top edge to bottom
3) WW (Warped world): if drunk moves past right-most edge, ends up on the top edge & vice versa.
                if moves past left edge, ends up on bottom edge & vice versa
4) BH (back to home): whenever drunk reaches any edge, gets transpotrted back to center of world

'''

EDGES_HIT = 0 # edges hit as a count global var

# world class, like field, but contains fences
class EnclosedField(object):
    global EDGES_HIT

    def __init__(self, edges):
        '''
        :param edges: edges = [left, right, up, down]
        :return:
        '''
        self.drunks = {}
        self.edges = edges
        self.edgesHit = [] # hit edges

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            # drunk.setLocation(loc.x, loc.y)
            # drunk.setDirection((loc.x, loc.y))
            self.drunks[drunk] = loc

    def moveDrunk(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        currentLocation = self.drunks[drunk]
        # x = currentLocation.getX()
        # y = currentLocation.getY()
        nextStep = drunk.takeStep()
        xDist, yDist = self.moveWithinEnclosed(currentLocation, nextStep)

        # if self.edges[0] < x + xDist < self.edges[1] and self.edges[2] < y + yDist < self.edges[3]:
        nextLocation = currentLocation.move(xDist, yDist)
        self.drunks[drunk] = nextLocation
            #drunk.setLocation(nextLocation.x, nextLocation.y)

    def getEdgeHitCount(self):
        return len(self.edgesHit)

    def getEdges(self):
        return self.edges

    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

    def getDrunks(self):
        return self.drunks

    def getDrunkPosition(self, drunk):
        currLocation = self.drunks[drunk]
        return currLocation

    def getType(self):
        pass

    # # does nothing- subclasses implement this
    # def moveWithinEnclosed(self):
    #     pass

class SolidWallField(EnclosedField):

    def moveWithinEnclosed(self, currentLocation, steps):
        global EDGES_HIT
        leftEdge = self.edges[0]
        rightEdge = self.edges[1]
        bottomEdge = self.edges[2]
        topEdge = self.edges[3]
        dx, dy = steps # steps drunk potentially moves

        x = currentLocation.getX()
        y = currentLocation.getY()

        if x+dx > leftEdge and x+dx < rightEdge:
            x += dx
            EDGES_HIT += 1
        else:
            x = 0
        if  y+dy > bottomEdge and y+dy < topEdge:
            y += dy
            EDGES_HIT += 1
        else:
            y = 0

        return x, y

    def getType(self):
        return 'Solid Wall Field'

#goes back home if moves past edges/fences
class BackHomeField(EnclosedField):


    def moveWithinEnclosed(self, currentLocation, steps):
        global EDGES_HIT
        leftEdge = self.edges[0]
        rightEdge = self.edges[1]
        bottomEdge = self.edges[2]
        topEdge = self.edges[3]
        dx, dy = steps # steps drunk potentially moves

        x = currentLocation.getX()
        y = currentLocation.getY()

        if x+dx > leftEdge and x+dx < rightEdge:
            x += dx
            EDGES_HIT += 1
        elif x+dx > rightEdge:
            x = leftEdge + (x+dx - rightEdge)
            EDGES_HIT += 1
        elif x+dx < leftEdge:
            x = rightEdge - (leftEdge - (x+dx))
            EDGES_HIT += 1
        else:
            x = 0
        if  y+dy > bottomEdge and y+dy < topEdge:
            y += dy
            EDGES_HIT += 1
        elif y+dy > topEdge:
            y = bottomEdge + (y+dy - topEdge)
            EDGES_HIT += 1
        elif y+dy < bottomEdge:
            y = topEdge - (bottomEdge - (y+dy))
            EDGES_HIT += 1
        else:
            y = 0

        return x, y

    def getType(self):
        return 'Back to home field'

# goes around in circle (if past left, turns up right & vice versa)
class SmallPlanetField(EnclosedField):

    def moveWithinEnclosed(self, currentLocation, steps):
        global EDGES_HIT
        leftEdge = self.edges[0]
        rightEdge = self.edges[1]
        bottomEdge = self.edges[2]
        topEdge = self.edges[3]
        dx, dy = steps # steps drunk potentially moves

        x = currentLocation.getX()
        y = currentLocation.getY()

        if x+dx < rightEdge and x+dx > leftEdge:
            x += dx
            EDGES_HIT += 1
        elif x+dx > rightEdge:
            x = bottomEdge
            EDGES_HIT += 1
        elif x+dx < leftEdge:
            x = topEdge
            EDGES_HIT += 1
        else:
            x = 0
        if y+dy < topEdge and  y+dy > bottomEdge:
            y += dy
            EDGES_HIT += 1
        elif y+dy > topEdge:
            y = leftEdge
            EDGES_HIT += 1
        elif y+dy < bottomEdge:
            y = rightEdge
            EDGES_HIT += 1
        else:
            y = 0


        return x, y

    def getType(self):
        return 'Small Planet Field'

# like small planet, but if past left, ends up at top & vice versa
class WarpedWorld(EnclosedField):

    def moveWithinEnclosed(self, currentLocation, steps):
        global EDGES_HIT

        leftEdge = self.edges[0]
        rightEdge = self.edges[1]
        bottomEdge = self.edges[2]
        topEdge = self.edges[3]
        dx, dy = steps # steps drunk potentially moves

        x = currentLocation.getX()
        y = currentLocation.getY()

        if x+dx < rightEdge and x+dx > leftEdge:
            x += dx
            EDGES_HIT += 1
        elif x+dx > rightEdge:
            x = bottomEdge
            EDGES_HIT += 1
        elif x+dx < leftEdge:
            x = topEdge
            EDGES_HIT += 1
        else:
            x = 0
        if y+dy < topEdge and y+dy > bottomEdge:
            y += dy
            EDGES_HIT += 1
        elif y+dy > topEdge:
            y = leftEdge
            EDGES_HIT += 1
        elif y+dy < bottomEdge:
            y = rightEdge
            EDGES_HIT += 1
        else:
            y = 0

        return x, y

    def getType(self):
        return 'Warped World Field'