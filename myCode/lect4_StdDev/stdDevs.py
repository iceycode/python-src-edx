__author__ = 'Allen'




'''
Std Dev (from lecture)
'''
def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

#prints the SDs in lists below
def getSDs():
    X1 = (0,1,2,3,4,5,6)
    X2 = (3,3,3,3,3,3,3)
    X3 = (0,0,0,3,6,6,6)
    X3A = (0,0, 0, 3,6,6,)
    X4 = (3,3,4,7,7)
    X4A = (3,4,7,7)
    X5 = (1,5,5,5,9)
    print "X1 SD = ", str(stdDev(X1))
    print "X2 SD = ", str(stdDev(X2))
    print "X3 SD = ", str(stdDev(X3)) #largest SD
    print "X4 SD = ", str(stdDev(X4))
    print "X5 SD = ", str(stdDev(X5))
    print "X4A SD (compared to X4, 1 value removed) = " + str(stdDev(X4A))
    print "X3A SD (compared to X4, 1 value removed) = " + str(stdDev(X3A))

#getSDs()





'''
Takes a list of strings, L, outputs Std Dev of lengths of strings
returns float('NaN') if L is empty
'''
def stdDevOfLengths(L):
    '''
    :param L: list of strings
    :return: stdDev of the lengths of those words or NaN if L empty
    '''
    if (len(L)==0):
        return float('NaN')

    lengths = []
    for word in L:
        lengths.append(len(word))

    mean = sum(lengths)/float(len(lengths))
    tot = 0.0
    for x in lengths:
        tot += (x - mean)**2

    return (tot/len(lengths))**0.5


def testStdDevsOfWordLengths():
    #0. Test case empty list L0 = []
    L0 = []
    print "empty list std dev = " + str(stdDevOfLengths(L0))

    #1. Test case: If L = ['a', 'z', 'p'], stdDevOfLengths(L) = 0.
    L1 = ['a', 'z', 'p']
    print "Std Dev of lengths of words in L1 = ", str(stdDevOfLengths(L1))


    #2. Test case: If L = ['apples', 'oranges', 'kiwis', 'pineapples'], stdDevOfLengths(L) = 1.8708.
    L2 = ['apples', 'oranges', 'kiwis', 'pineapples']
    print "Std Dev of lengths of words in L2 = ", str(stdDevOfLengths(L2))

#testStdDevsOfWordLengths()








'''Coefficient of Variance
'''
def CV(X):
    mean = sum(X)/float(len(X))
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('NaN')


def testCVs():
    L1 = [1,2,3]
    print 'L1 CV = ', str(CV(L1))
    L2 = [11,12,13]
    print 'L2 CV = ', str(CV(L2))
    L3 = [.1,.1,.1]
    print 'L3 CV = ', str(CV(L3))
    L4 = [10, 4, 12, 15, 20, 5]
    print str(L4 ), ' CV = ', str(CV(L4))

#tests for Coefficient of Variation problems
testCVs()

