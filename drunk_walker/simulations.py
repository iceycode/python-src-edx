__author__ = 'Allen'

import pylab, Field
from Drunk import *
from Field import *
import DrunkVisualize

# function for random walk calculation of actual x & y distance
def walkVector(f, d, numSteps):
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(f.getLoc(d).getX() - start.getX(),
           f.getLoc(d).getY() - start.getY())



# simulates drunk walking for N trials
def simWalks(numSteps, numTrials, dClass):
    homer = dClass('Homer')
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(homer, origin)
        distances.append(walkVector(f, homer, numSteps))
    return distances


def drunkTest_diffClasses(numTrials = 100):
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

#drunkTest_diffClasses()



# a simulation with drunk animations
def simWithAnimation(numSteps, f, dClass, testNum):
    homer = dClass('Homer')
    origin = Location(0, 0)
    xAxis = []
    yAxis = []
    f.addDrunk(homer, origin)
    # anim = DrunkVisualize.DrunkVisualize(f)

    # move & animated drunk
    for s in range(numSteps):
        f.moveDrunk(homer)
        x, y = f.drunks[homer].getX(), f.drunks[homer].getY()
        xAxis.append(x)
        yAxis.append(y)
        # anim.update(f, f.getDrunks())
        print f.drunks[homer]
    # anim.done()

    pylab.title('Steps Drunk Took Within Field: ' + f.getType())
    pylab.figure(testNum)
    pylab.xlim(-60, 60)
    pylab.ylim(-60, 60)
    pylab.plot(xAxis, yAxis, 'ro')

'''
N-random steps: drunk takes N*N random steps with following:
    dx,dy = random.choice(
        [(-1.0,-1.0),(-1.0,0.0),(-1.0,1.0),(0.0,1.0),(0.0,-1.0),(1.0,-1.0))
        (1.0,0.0),(1.0,1.0)]
    )

Assume the drunk walks for long enough that he has reached a wall.
A mark is made on the graph for each position that the drunk occupies.
For each of the graphs, indicate which type of walls (SW, SP, WW, or BH) bound the field.
Create a graph showing all times drunk bumps into a wall
'''

# testing drunk movement by plotting times drunk hits edge
def drunkTest_enclosedField():
    edges = [-60, 60, -60, 60] # [left, right, bottom, top]
    dClass = TrappedDrunk
    fields = [SolidWallField(edges), SmallPlanetField(edges), BackHomeField(edges), WarpedWorld(edges)]

    for i in xrange(len(fields)):
        simWithAnimation(5000, fields[i], dClass, i)

    simWithAnimation(5000, fields[0], dClass, i)

    pylab.show()

drunkTest_enclosedField()
