__author__ = 'Allen'

from Field import *
import random, math


class Drunk(object):
    def __init__(self, name):
        self.name = name
        self.direction = 0

    def setLocation(self, x, y):
        self.location = x, y

    def getLocation(self):
        return self.location

    #sets the direction of drunk (360 deg)
    def setDirection(self, next):
        x, y = self.getLocation()
        dx, dy = next
        if x > dx and y == dy:
            self.direction = 180 # move left
        elif x < dx and y == dy:
            self.direction = 360 # move right
        elif y > dy and x == dx:
            self.direction = 270 # move down
        elif y < dy and x == dx:
            self.direction =  90 # move up
        elif x > dx and y > dy:
            self.direction = 215 # move left, down
        elif x < dx and y < dy:
            self.direction = 45 # move right, up
        elif y < dy and x > dx:
            self.direction = 135# move left, up
        elif y > dy and x < dx:
            self.direction = 315 # move right, down
        else:
            self.direction = 0 # do no change direction

    def getDirection(self):
        return self.direction

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
        newStep = random.choice(stepChoices)
        self.setDirection(newStep)
        return newStep

class EDrunk(Drunk):
    def takeStep(self):
        ang = 2 * math.pi * random.random()
        length = 0.5 + 0.5 * random.random()
        newStep = (length * math.sin(ang), length * math.cos(ang))
        self.setDirection(newStep)
        return newStep

class PhotoDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.0, 0.5),(0.0, -0.5),
                     (1.5, 0.0),(-1.5, 0.0)]
        newStep = random.choice(stepChoices)
        self.setDirection(newStep)
        return newStep

class DDrunk(Drunk):
    def takeStep(self):
        stepChoices =\
                    [(0.85, 0.85), (-0.85, -0.85),
                     (-0.56, 0.56), (0.56, -0.56)]
        newStep = random.choice(stepChoices)
        # self.setDirection(newStep)
        return newStep


# a drunk in an enclosed area
class TrappedDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(-1.0,-1.0),(-1.0,0.0), #(left, down), (left, stay)
                         (-1.0,1.0),(0.0,1.0), # (left, up), (stay, up)
                         (0.0,-1.0),(1.0,-1.0), # (stay, down), (right, down)
                         (1.0,0.0),(1.0,1.0)] # (right, stay), (right, up)
        newStep = random.choice(stepChoices)
        # self.setDirection(newStep)
        return newStep
