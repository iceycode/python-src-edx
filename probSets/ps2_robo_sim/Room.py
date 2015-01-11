__author__ = 'Allen'
import math
import random
import Position
'''
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
'''

# === Problem 1
class Room(object):

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
        #random.seed(0)
        randX = random.randrange(0, self.width)
        randY = random.randrange(0, self.height)
        return Position(randX, randY)

    def isPositionInRoom(self, pos):
        '''
        * Return True if pos is inside the room.
        :param pos:  a Position object.
        :return: True if pos is in the room, False otherwise.
        '''
        # if pos.getX() in range(0, self.width) and pos.getY() in range(0, self.height):
        #     return True

        if 0 <= pos.getX()<float(self.width) and 0 <= pos.getY() < float(self.height):
            return True
        else:
            return False