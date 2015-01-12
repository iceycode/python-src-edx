import random


class intDict(object):
    """A dictionary with integer keys"""
    
    def __init__(self, numBuckets):
        """Create an empty dictionary"""
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])

    '''
    takes key & hashing into hashBucket based on size of the bucket
    if finds a value returns; if not appends with value
    '''
    def addEntry(self, dictKey, dictVal):
        """Assumes dictKey an int.  Adds an entry."""
        hashBucket = self.buckets[dictKey%self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == dictKey:
                print 'previous dictValue = ', str(hashBucket[i][1])
                hashBucket[i] = (dictKey, dictVal)
                print "a collision took place \ndictKey = ", str(dictKey), '\ndictVal = ', str(dictVal)

                return
        hashBucket.append((dictKey, dictVal))


    #works like addEntry
    def getValue(self, dictKey):
        """Assumes dictKey an int.  Returns entry associated
           with the key dictKey"""
        hashBucket = self.buckets[dictKey%self.numBuckets]
        for e in hashBucket:
            if e[0] == dictKey:
                return e[1]
        return None
    
    def __str__(self):
        res = '{'
        for b in self.buckets:
            for t in b:
                res = res + str(t[0]) + ':' + str(t[1]) + ','
        return res[:-1] + '}' #res[:-1] removes the last comma


D = intDict(29)
for i in range(20):
    #choose a random int in range(10**5) <--becomes key
    key = random.choice(range(22 ))
    D.addEntry(key, i) #



'''
get 29 buckets, some have multiple entries, some empty
- don't have as many collisions
'''
print '\n', 'The buckets are:'
for hashBucket in D.buckets: #violates abstraction barrier
    print '  ', hashBucket















