__author__ = 'Allen'
__doc__ = "Exam 1 (Quiz) code"

import random, pylab



def randDistribution():
    randomList1 = []
    for i in range(1000):
        randomList1.append(int(random.random() * 2))

    randomList2 = []
    for i in range(1000):
        randomList2.append(random.choice((0,1)))

    count1A = []
    count0A = []
    count1B = []
    count0B = []
    for i in range(1000):
        if randomList1[i] == 1:
            count1A.append(randomList1[i])
        else:
            count0A.append(randomList1[i])

        if randomList2[i] == 1:
            count1B.append(randomList2[i])
        else:
            count0B.append(randomList2[i])

    print "count of randomList1 1s = ", len(count1A)
    print "count of randomList1 0s = ", len(count0A), "\n"
    print "count of randomList2 1s = ", len(count1B)
    print "count of randomList2 0s = ", len(count0B), "\n"

#randDistribution() #NOT THE SAME DISTRIBUTION OF 1s & 0s

def pylabTest():
    xVals = []
    yVals = []
    wVals = []
    for i in range(1000):
        xVals.append(random.random())
        yVals.append(random.random())
        wVals.append(random.random())
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    wVals = pylab.array(wVals)
    xVals = xVals + xVals
    zVals = xVals + yVals
    tVals = xVals + yVals + wVals

    #pylab.plot(xVals, yVals)
    #pylab.hist(tVals, bins=1000) #show normal distribution
    #pylab.plot(sorted(xVals), yVals)
    #pylab.plot(xVals, sorted(yVals))
    pylab.plot(sorted(xVals), sorted(tVals))
    pylab.show()

# pylabTest()





#a monte carlo simulation estimates student having final score >=70 & <=75
def sampleQuizes():
    '''
    Uniform distributions
    25% for midterm, 50% for final
    Midterm1: 50<= grad <= 80
    Midterm2: 60<=grad<=90
    Final: 55<=grade <= 95
    :return: prob of score >=70 & <=75
    '''
    numTrials = 10000
    countGrade = 0.0 #counts number of times between 70 & 75 (inclusive)
    for i in xrange(numTrials):
        mid1 = random.randrange(50, 81)
        mid2 = random.randrange(60, 91)
        final = random.randrange(55, 96)
        total = (mid1 + mid2)*.25 + final*.5
        if 70 <= total <= 75:
            countGrade += 1.0

    return countGrade/numTrials


# print "mid1 = ", mid1, "\nmid2 = ", mid2, "\n final = ", final, "\n total = ", total
# print "is between 70 & 75", countGrade

def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of
    the three exams, then calculates the final score and
    appends it to a list of scores.

    Returns: A list of numTrials scores.
    """
    scores = []
    for i in xrange(numTrials):
        mid1 = random.randrange(50, 81)
        mid2 = random.randrange(60, 91)
        final = random.randrange(55, 96)
        total = (mid1 + mid2)*.25 + final*.5
        scores.append(total)

    return scores

def plotQuizzes():
    scores = generateScores(10000)
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of Trials')
    pylab.title('Distribution of Scores')
    pylab.hist(scores, bins = 7)
    pylab.show()


#plotQuizzes()


#returns number of occurences until limit is seen
def probTest(limit):
    n = 0 #number of rolls
    roll1 = 1.0/6.0
    rollOther = 1.0 - roll1
    prob = 1.0 #start out at 1.0
    while prob >= limit:
        prob = (rollOther**n) * roll1
        n += 1

    return n

print probTest(.5)


#random balls, white if 1, else black
#it is white if 1


def lvMethod(balls):
    count = 0
    ball = 0 #set to being black (not white initially
    while ball != 1:
        count += 1
        rand_ball = random.randrange(0, 1000)
        ball = balls[rand_ball]


    return count


def mcMethod(balls, tries = 1000):
    numTries = 0
    ball = 0 #initialize ball
    while ball != 1:
        ball = balls[random.randrange(0, len(balls))] #points to random locations
        if ball == 1 and numTries==0:
            return 1
        elif ball == 1 and numTries > 0:
            return numTries
        numTries += 1

    return 0


def plotTries1():
    balls = []
    for i in range(1000):
        ball = random.choice((0,1))
        balls.append(ball)

    histogram = [ 0 for i in range(1,1000)]  # intialize the list to be all zeros
    for i in range(1000):
        result = lvMethod(balls)
        histogram[result] += 1

    pylab.plot(histogram)
    pylab.xlim(0,10)
    pylab.show()

def plotTries2():
    balls = []
    for i in range(1000):
        ball = random.choice((0,1))
        balls.append(ball)

    histogram = [ 0 for i in range(1,1000)]  # intialize the list to be all zeros
    for i in range(1000):
        result = mcMethod(balls)
        histogram[result] += 1

    pylab.plot(histogram)
    pylab.xlim(0,10)
    pylab.show()

# plotTries1()
#plotTries2()