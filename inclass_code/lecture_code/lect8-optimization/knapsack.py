import pylab
'''
Lecture 8: Optimization Problems
- Knapsack Problem as example
- Finding/Sorting
- Trees
- Memoization (see memoization.py)
- Algorithms used
   - Greedy
   - Best
   - Trees
'''

#Item object burglar can carry in knapsack
class Item(object):
    def __init__(self, n, v, w):
        '''
        Values
        :param n: name of item
        :param v: value of item
        :param w: weight of item
        '''
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) + ', '\
                 + str(self.weight) + '>'
        return result

#helper function for building Item list
def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book',
             'computer']
    vals = [175,90,20,50,10,200]
    weights = [10,9,4,2,1,20]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    return Items

#has upper bound of O(nlog(n))
def greedy(Items, maxWeight, keyFcn):
    '''
    Greedy algorithm
    :param Items: list of items
    :param maxWeight: maximum weight
    :param keyFcn:
    :return:
    '''
    assert type(Items) == list and maxWeight >= 0 #checks list
    #takes list of item & ues keyFcn to tell value, reve
    ItemsCopy = sorted(Items, key=keyFcn, reverse = True)
    result = [] #items that will be stuffed in
    totalVal = 0.0
    totalWeight = 0.0
    i = 0
    #while item list not full & totalWeight not maxWeight
    while totalWeight < maxWeight and i < len(Items):
        if (totalWeight + ItemsCopy[i].getWeight()) <= maxWeight:
            result.append((ItemsCopy[i]))
            totalWeight += ItemsCopy[i].getWeight()
            totalVal += ItemsCopy[i].getValue()
        i += 1
    return (result, totalVal)

#helper functions for Greedy algorithm
def value(item):
    return item.getValue()

def weightInverse(item):
    return 1.0/item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()

def testGreedy(Items, constraint, getKey):
    '''
    Runs greedy with arguments, prints items taken
    :param Items: the items
    :param constraint: the constraint (weight)
    :param getKey: the value key
    '''
    taken, val = greedy(Items, constraint, getKey)
    print ('Total value of items taken = ' + str(val))
    for item in taken:
        print '  ', item

def testGreedys(maxWeight = 20):
    '''
    tests Greedy algorithm based on contstraints
    :param maxWeight: max weight sack can carry
    '''
    Items = buildItems()
    print('Items to choose from:')
    for item in Items:
        print '  ', item
    #based simply on higest value
    print 'Use greedy by value to fill a knapsack of size', maxWeight
    testGreedy(Items, maxWeight, value)

    #based on weight, lightest to heaviest
    print 'Use greedy by weight to fill a knapsack of size', maxWeight
    testGreedy(Items, maxWeight, weightInverse)

    #based on density of items (how much space they take)
    print 'Use greedy by density to fill a knapsack of size', maxWeight
    testGreedy(Items, maxWeight, density)


#testGreedys()



#--BRUTE FORCE--

#converts digital to binary number
# allows binary representations of power set
def dToB(n, numDigits):
    """requires: n is a natural number less than 2**numDigits
      returns a binary string of length numDigits representing the
              the decimal number n."""
    assert type(n)==int and type(numDigits)==int and n >=0 and n < 2**numDigits
    bStr = ''
    while n > 0:
        bStr = str(n % 2) + bStr #convert higest order bit to string ; add to bStr
        n = n//2
    #if room is still left over; puts 0 in front of bStr
    while numDigits - len(bStr) > 0:
        bStr = '0' + bStr
    return bStr

#print dToB(5, 4) #shows 0101
print dToB(16, 8) #shows 00010000


#the power set of items (all possible combinations)
def genPset(Items):
    """Generate a list of lists representing the power set of Items"""
    numSubsets = 2**len(Items)
    templates = [] #template of how to include things
    for i in range(numSubsets):
        templates.append(dToB(i, len(Items)))
    pset = []

    #whether to include in set
    for t in templates:
        elem = []
        for j in range(len(t)): #if it is element, include it
            if t[j] == '1':
                elem.append(Items[j])
        pset.append(elem) #append to powerset
    return pset #returns all the sets

#chooses best solution from power set
def chooseBest(pset, constraint, getVal, getWeight):
    bestVal = 0.0
    bestSet = None
    for Items in pset:
        ItemsVal = 0.0
        ItemsWeight = 0.0
        for item in Items:
            ItemsVal += getVal(item)
            ItemsWeight += getWeight(item)
        # test against constraint & best value so far
        if ItemsWeight <= constraint and ItemsVal > bestVal:
            bestVal = ItemsVal
            bestSet = Items
    return (bestSet, bestVal)

#test brute force solution to finding best power set
def testBest():
    Items = buildItems()
    pset = genPset(Items)
    taken, val = chooseBest(pset, 20, Item.getValue, Item.getWeight)
    print ('Total value of items taken = ' + str(val))
    for item in taken:
        print '  ', item

#testBest() #value is 275.0; is optimal




#--------Decision Tree Solution----------

# Recursive function to check items along tree
#
# considered element; available element
# consider
def maxVal(toConsider, avail):
    #when there is none available (list contains nothing)
    if toConsider == [] or avail == 0:
        result = (0, ())
    #consider others
    elif toConsider[0].getWeight() > avail:
        result = maxVal(toConsider[1:], avail)
    #if there is room
    else:
        nextItem = toConsider[0]

        #Explore left branch
        withVal, withToTake = maxVal(toConsider[1:],
                                      avail - nextItem.getWeight())
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)

        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def smallTest():
    Items = buildItems()
    val, taken = maxVal(Items, 20)
    for item in taken:
        print(item)
    print ('Total value of items taken = ' + str(val))


smallTest()
