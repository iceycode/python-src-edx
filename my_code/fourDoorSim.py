__author__ = 'Allen'

'''
Simulation that is similar to Monty Hall Problem
4 doors, 2 cars, 2 goats instead
Player chooses door, host chooses door (knows it or not)
'''
import pylab
import random

def hostChoose(guessDoor, prizeDoor1, prizeDoor2):
    '''
    Monty KNOWS door
    :param guessDoor:
    :param prizeDoor:
    :return:
    '''
    if 1 != guessDoor and 1 != prizeDoor1 and 1 != prizeDoor2:
        return 1
    if 2 != guessDoor and 2 != prizeDoor1 and 2 != prizeDoor2:
        return 2
    if 3 != guessDoor and 3 != prizeDoor1 and 3 != prizeDoor2:
        return 3
    return 4


def randomPrizeDoors(doorChoices):
    '''
    returns the 2 winning doors (rest are not)
    :param doorChoices:
    :return:
    '''
    prizeDoor1 = random.choice(doorChoices)
    doorChoices.remove(prizeDoor1)
    prizeDoor2 = random.choice(doorChoices)
    return (prizeDoor1, prizeDoor2)


def simMontyHall(numTrials):
    stickWins, switchWins, noWin = (0, 0, 0)

    for t in range(numTrials):
        prizeDoorChoices = [1,2,3,4]
        guessChoices = [1,2,3,4]
        pDoor1, pDoor2 = randomPrizeDoors(prizeDoorChoices)

        guess = random.choice(guessChoices) #choose but DO NOT OPEN
        guessChoices.remove(guess)
        toOpen = hostChoose(guess, pDoor1, pDoor2) #host chooses & OPENS door
        guessChoices.remove(toOpen) #remove this door as option of doors to remove

        guess2 = random.choice(prizeDoorChoices) #2nd optional guess

        if guess == pDoor1 or guess == pDoor2:
            stickWins += 1
        elif guess2 == pDoor1 or guess2 == pDoor2:
            switchWins+=1
        else:
            noWin+=1

    return (stickWins, switchWins)



def displayMHSim(simResults, title):
    stickWins, switchWins = simResults
    pylab.pie([stickWins, switchWins],
              colors = ['r', 'c'],
              labels = ['stick', 'change'],
              autopct = '%.2f%%')
    pylab.title(title)

simResults = simMontyHall(100000)
displayMHSim(simResults, 'Monty Chooses a Door w/ GOAT')
pylab.show()
#pylab.figure()
#simResults = simMontyHall(10000, randomChoose)
#displayMHSim(simResults, 'Door Chosen at Random')

