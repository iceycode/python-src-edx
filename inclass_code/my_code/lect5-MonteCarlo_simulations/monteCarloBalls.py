__author__ = 'Allen'

'''
Have 3 Red & 3 Green balls, each time draw, DO NOT REPLACE
What is probability of drawing 3 balls of same color?
'''
import random

def chooseBall(balls):
    return random.choice(balls)

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    sameColor = 0.0 #keeps track of same ball color
    for i in range(numTrials):
        balls = [1, 2, 3, 4, 5, 6] #1-3 are red, 4-6 are green
        b1 = random.choice(balls)
        balls.remove(b1)
        b2 = random.choice(balls)
        balls.remove(b2)
        b3 = random.choice(balls)
        if (b1 < 4 and b2 < 4 and b3 < 4) or (b1>3 and b2>3 and b3>3):
            sameColor += 1

    return sameColor/numTrials


'''
2 balls drawn with replacement
probability of 1st blue, 2nd red
'''
def randomBallsMonteCarlo(numTrials):
    orderDraw = 0.0
    for i in range(numTrials):
        balls = [1,2,3,4,5,6,7,8] #1 : green; 2-3-red; 4-8: blue
        b1 = random.choice(balls)
        b2 = random.choice(balls)
        if (4<=b1<=8) and (2<=b2<=3):
            orderDraw+=1

    return orderDraw/numTrials


print "Probability of 3 balls of same color (3 red, 3 green) = ", noReplacementSimulation(5000)
print "Probability of 1st ball ball, 2nd red w/ replacement (1 green, 2 red, 5 blue) = ", randomBallsMonteCarlo(4000)