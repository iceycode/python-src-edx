import random

class intDict(object):
    """A dictionary with integer keys"""
    
    def __init__(self, numBuckets):
        """Create an empty dictionary"""
        self.buckets = []
        self.numBuckets = numBuckets
        self.num_collisions = 0 # tracks collisions
        for i in range(numBuckets):
            self.buckets.append([])
            
    def addEntry(self, dictKey, dictVal):
        """Assumes dictKey an int.  Adds an entry."""
        hashBucket = self.buckets[dictKey%self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == dictKey:
                hashBucket[i] = (dictKey, dictVal)
                self.num_collisions += 1
                return
        hashBucket.append((dictKey, dictVal))
        
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




def collision_prob(numBuckets, numInsertions):
    '''
    Given the number of buckets and the number of items to insert, 
    calculates the probability of a collision.
    '''
    prob = 1.0
    for i in range(1, numInsertions):
        prob = prob * ((numBuckets - i) / float(numBuckets))
    return 1 - prob



def sim_insertions(numBuckets, numInsertions):
    '''
    Run a simulation for numInsertions insertions into the hash table.
    '''
    choices = range(numBuckets)
    used = []
    for i in range(numInsertions):
        hashVal = random.choice(choices)
        if hashVal in used:
            return False
        else:
            used.append(hashVal)
    return True


def observe_prob(numBuckets, numInsertions, numTrials):
    '''
    Given the number of buckets and the number of items to insert, 
    runs a simulation numTrials times to observe the probability of a collision.
    '''
    probs = []
    bd_coll = 0 # number of collision (for student b-day problem)
    for t in range(numTrials):
        col = sim_insertions(numBuckets, numInsertions)

        probs.append(col)

    return 1 - sum(probs)/float(numTrials)

#original main function
def main():
    hash_table = intDict(25)
    hash_table.addEntry(15, 'a')
#    random.seed(1) # Uncomment for consistent results
    for i in range(20):
       hash_table.addEntry(int(random.random() * (10 ** 9)), i)
    hash_table.addEntry(15, 'b')
    print hash_table.buckets  #evil
    print '\n', 'hash_table =', hash_table
    print hash_table.getValue(15)


'''
MODIFIED main function
Added default values of
'''
def my_main_test(numBuckets = 365, numInsertions = 30):
    #hash_table = intDict(25)
    hash_table = intDict(numBuckets)
    hash_table.addEntry(numInsertions, 'a')
#    random.seed(1) # Uncomment for consistent results
    for i in range(numInsertions):
       hash_table.addEntry(int(random.random() * (10 ** 9)), i)
    #hash_table.addEntry(15, 'b')
    print hash_table.buckets  #evil
    print '\n', 'hash_table =', hash_table
    #print hash_table.getValue(15)


def largest_contains_a_collision():
    '''
    Given 365 days & P(two students share B-day),
    what is largest amount of students (insertions) in which
    prob would be less then .99
    '''
    numBuckets = 365
    max_insertions = 250 #at this number probability is .99
    for i in range(1, max_insertions):
        #my_main_test(numInsertions=500)
        prob = collision_prob(numBuckets, i)
        if prob < .99 :
            print 'number of insertions (students) = ', str(i)


#Test probabilities here
print '(1): P(collision) if 1000 buckets, 50 insertions'
print str(collision_prob(1000, 50)) # P(collision) = 0.712

print '(2): P(collision) 1000 buckets & 200 insertions' #0.999
print str(collision_prob(1000, 200))

print '(3): P(collision) 1000 buckets, 50 insertions, 1000 trials'  #0.71
print str(observe_prob(1000,50, 1000))

print('(4): P(collision) 1000 buckets, 200 insertions, 1000 trials') #1.000
print str(observe_prob(1000, 200, 1000))

print '(5): P(2 students share same birthday); 30 students, 365 days'
print str(collision_prob(365, 30)) #0.412


print '(6): P(2 students share same birthday); 250 students, 365 days'
print str(collision_prob(365, 250)) #1.000


print'(7): largest number of students so that P(2 stud share b-day) < .99'
largest_contains_a_collision()



'''
        col = sim_insertions(numBuckets, numInsertions)
        if (col==False) :
            bd_coll+=1

        if bd_coll==2 :
            return bd_coll
'''