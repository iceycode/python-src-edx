__author__ = 'Allen'
"""
Generates a powerset or bits from items
"""
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



def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book',
             'computer']
    vals = [175,90,20,50,10,200]
    weights = [10,9,4,2,1,20]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    return Items

# EXAMPLES OF POWERSET GENERATORS USING BINARY NUMS
# generate all combinations of N items
# 0 = not in list;
# 1 = in list
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in xrange(2**N):
        combo = []
        for j in xrange(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

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

# a generator that returns every combo of objects in 1 bag
# returns 1s & 0s denoting whether they are in the bag
# NOTES: (see python docs for more about bitwise operators)
#
# x << y : returns x with bits shifted to left by y places
# x >> y : same as about but shifted to right (same as //'ingx by 2**y
# x & y : "bitwise and"; each is 1 if x & y corresponding bits are 1
# x | y : "bitwise or" ; each is 0.....
# ~x : returns complement of x (0s & 1s switched)
# x ^ y : "bitwise exclusive or"; each bit of output is same as corresponding x if that bit in y is 0
#               & complement of bit in x if that bit in y is 1
#
# with 2 bags, there exist 3^n possible combinations
# with 1 bag; item either in bag or not; so 0 or 1; & N items
# with 2 bags; 0, 1, or 2; 0= not in bag; 1 = in bag1; 2 = in bag2


def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as
      a list of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in xrange(3**N):
        bag1 = []
        bag2 = []
        for j in xrange(N):
            # test bit jth of integer i
            if (i/(3**j))%3 == 1:
                bag1.append(items[j])
            elif (i/(3**j))%3 == 2:
                bag2.append(items[j])
            yield (bag1, bag2)

items = buildItems()
print yieldAllCombos(items)
