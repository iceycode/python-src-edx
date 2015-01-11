#__author__ = 'Allen'

# Uncomment this line to see your implementation of StandardRobot in action!
##testRobotMovement(StandardRobot, RectangularRoom)
import random
import Room
import Position


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
        #random.seed(0) #for debugging purposes
        randDir = random.randrange(1, 361)
        self.setRobotDirection(randDir)
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

