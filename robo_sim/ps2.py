# 6.00.2x Problem Set 2: Simulating robots

'''
Simulates a robot (similar to a roomba moving around a room


'''
import math
import random

import pylab



# For Python 2.7:

#from probSets.robo_sim.robo_sim.ps2_verify_movement27 import testRobotMovement

#import testRobotMovement

# If you get a "Bad magic number" ImportError, you are not using 
# Python 2.7 and using most likely Python 2.6:


# === Provided class Position
from robo_sim import ps2_visualize


class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):

    def __init__(self, width, height):
        '''
        * Initializes a rectangular room with the specified width and height.
        * Initially, no tiles in the room have been cleaned.

        :param width: an integer > 0
        :param height: an integer > 0
        '''
        self.width = width # x-axis
        self.height = height # y-axis
        self.tiles = [] #initialize tile list of tiles as Position objects
        self.tilesCleaned = [] #initialize list of cleaned tiles
        for w in range(0, width):
            for h in range(0, height):
                self.tiles.append([w,h])


    def cleanTileAtPosition(self, pos):
        '''
        * Mark the tile under the position POS as cleaned.
        * Assumes that POS represents a valid position inside this room.
        :param pos: a Position
        '''
        posX = math.floor(pos.getX())
        posY = math.floor(pos.getY())
        for tile in self.tiles:
            if posX==tile[0] and posY==tile[1] and self.isTileCleaned(posX,posY)==False:
                self.tilesCleaned.append(tile)


    def isTileCleaned(self, m, n):
        '''
        Assumes that (m, n) represents a valid tile inside the room.

        :param m: an integer
        :param n: an integer
        :return: True if the tile (m, n) has been cleaned, otherwise False
        '''
        for tile in self.tilesCleaned:
            if m==tile[0] and n==tile[1]:
                return True

        return False

    def getNumTiles(self):
        '''
        :return: an integer, total number of tiles in the room.
        '''
        return len(self.tiles)

    def getNumCleanedTiles(self):
        '''
        :return: an integer, total number of clean tiles in the room.
        '''
        return len(self.tilesCleaned)

    def getRandomPosition(self):
        '''
        :return: a Position object (random position)
        '''
        #random.seed(0) #for debugging purposes
        randX = random.randrange(0, self.width)
        randY = random.randrange(0, self.height)

        return Position(randX, randY)

    def isPositionInRoom(self, pos):
        '''
        * Return True if pos is inside the room.
        :param pos:  a Position object.
        :return: True if pos is in the room, False otherwise.
        '''
        if 0 <= pos.getX()< float(self.width) and 0 <= pos.getY() < float(self.height):
            return True
        else:
            return False


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        '''
        Initializes a Robot with the given speed in the specified room.
        The robot initially has a random direction and a random position in the room.
        The robot cleans the tile it is on.
        :param room:
        :param speed:
        '''
        self.room = room
        self.speed = speed
        self.setRobotPosition(room.getRandomPosition())
        self.setRobotDirection(random.randrange(1, 361))
        self.room.cleanTileAtPosition(self.getRobotPosition())


    def getRobotPosition(self):
        '''
        Return the position of the robot.
        :returns: a Position object giving the robot's position.
        '''
        return self.position

    def getRobotDirection(self):
        '''
        Return the direction of the robot.

        :returns: an integer d giving the direction of the robot as an angle in
                    degrees, 0 <= d < 360.
        '''
        return self.direction

    def setRobotPosition(self, position):
        '''
        Set the position of the robot to POSITION.

        :param: a Position object.
        '''
        self.position = position

    def setRobotDirection(self, direction):
        '''
        Set the direction of the robot to DIRECTION.

        :param: direction: integer representing an angle in degrees
        '''
        self.direction = direction

    def updatePositionAndClean(self):
        '''
        Simulate the raise passage of a single time-step.
        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        '''
        raise NotImplementedError # don't change this!





# === Problem 2 - subclass of Robot
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        '''
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        '''
        nextPos = self.getRobotPosition().getNewPosition(self.getRobotDirection(), self.speed)

        if self.room.isPositionInRoom(nextPos)==True:
            self.setRobotPosition(nextPos)
            self.room.cleanTileAtPosition(self.getRobotPosition())
        else:
            self.setRobotDirection(random.randrange(1,365))

# Uncomment this line to see your implementation of StandardRobot in action!
#testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 4
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        '''
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        '''
        nextPos = self.getRobotPosition().getNewPosition(self.getRobotDirection(), self.speed)
        self.setRobotDirection(random.randrange(1,365))

        if self.room.isPositionInRoom(nextPos)==True:
            self.setRobotPosition(nextPos)
            self.room.cleanTileAtPosition(self.getRobotPosition())



#testRobotMovement(RandomWalkRobot, RectangularRoom)

#returns the subclass type of Robot being used
class robot_type(Robot):
    def get_subclass_name(self):
        return self.__class__.__name__

# === Problem 3
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    totalSteps = 0.0 #the total time steps for robots int all trials

    for trial in range(1, num_trials+1):
        #comment all anim methods out for problem 5
        anim = ps2_visualize.RobotVisualization(num_robots, width, height, delay=.01) #animation for debugging
        timeSteps = 0.0 #set time steps to 0.0
        robots = [] #empty list of robots
        room = RectangularRoom(width, height) #room being used
        for i in range(1, num_robots+1):
            robots.append(robot_type(room, speed))

        #while room is not clean
        while float(room.getNumCleanedTiles())/float(room.getNumTiles()) < float(min_coverage):
            anim.update(room, robots)
            for robot in robots :
                robot.updatePositionAndClean()
            timeSteps += 1.0

        totalSteps += timeSteps #add to average of time steps
        anim.done()

    avg = totalSteps/num_trials
    #for testing purposes (DON'T use print method, or else answer incorrect)
    print "NumRobots: ", str(num_robots), " Speed: ", str(speed), "Min Covered Ratio: ", str(float(min_coverage)), "" \
            "; Num trials: ", str(num_trials), "; Avg clock ticks: ", avg

    return avg



# Uncomment this line to see how much your simulation takes on average
#avg = runSimulation(10, 1.0, 15, 20, 0.8, 30, StandardRobot)
#some references:
# 1 robot takes ~150 clock ticks to clean 100% of 5x5 room <-----PASSED
#avg = runSimulation(1, 1.0, 5, 5, 1.0, 11, RandomWalkRobot)
# 1 robot takes ~190 clock ticks to clean 75% of 10x10 room <------PASSED
#avg = runSimulation(1, 1.0, 10, 10, .75, 11, StandardRobot)
# 1 robot takes ~310 ticks to clean 90% of 10x10 room <-----PASSED
#avg = runSimulation(1, 1.0, 10, 10, 0.9, 11, StandardRobot)
# 1 robot takes ~3322 ticks to clean 100% a 20x20 room <----PASSED
#avg = runSimulation(1, 1.0, 20, 20, 1.0, 5, StandardRobot)
# 3 robot take ~1105 ticks to clean 100% of 20x20 room <----PASSED
#avg = runSimulation(3, 1.0, 10, 10, 1.0, 1, RandomWalkRobot)
#print "Average clock ticks ", str(avg)




def showPlot1(title, x_label, y_label):
    """
    average time takes different numbers of different kinds of robots
    to clean 80% of a 20x20 size room (over 20 trials)
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print "Plotting", num_robots, "robots..."
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    Shows times it takes for 2 robots to clean 80% of a variously shaped rooms
    x-axis: aspect-ratio (shape)
    y-axis:
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300/width #so width*height always equals 300
        print "Plotting cleaning time for a room of width:", width, "by height:", height
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 20, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 20, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    

# === Problem 5
#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#Best title for the graphyt
#showPlot1("Time it take 1 - 10 Robots to Clean 80% of a Room", "Number of Robots", "Time Steps")

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#showPlot2("Time it takes Two Robots to Clean 80% of variously shaped rooms", "Aspect Ratio", "Time-steps")