'''
Created on Oct 24, 2014

@author: Allen
'''
import random
import math
'''
Generates a random even number with range 0<=x<=100
generate a uniform distribution over the even numbers between 0 & 100 (not including 100).

'''
def genEven():
    return random.randrange(0,100,2) #returns even integer b/w 0 & 99





'''
returns a deterministically generated even number b/w 9 & 21
'''
def deterministicNumber():
    random.seed(1) #use to set starting integer value when generating
    return random.randrange(9,22) #returns even number between 9 & 21    

#Possible solutions:
def deterministicNumber1():
    return 10 # or 12 or 14 or 16 or 18 or 20


def deterministicNumber2():
    random.seed(0) # This will be discussed in the video "Drunken Simulations"
    return 2 * random.randint(5, 10)




'''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
'''
def stochasticNumber():
    #return random.choice(range(uniformRand,1))
    r = int((21-9)*random.random())
    if r%2==0 :
        return r + 10
    else:
        return r + 9

# Possible solutions:
def stochasticNumber1():
    return 2 * random.randint(5, 10)

# or 

def stochasticNumber2():
    return random.randrange(10, 22, 2)

# or, again, something like that.


'''
Tests for random number generator methods
'''
def testRandGen():
    for i in range(10):
        #r = genEven()
        #dr = deterministicNumber()
        #print( 'uniformily generatored rand even num: ' + str(r))
        
        #print('deterministically generated even number : ' + str(dr))
        print('stochiastically generated even number ' + str(stochasticNumber()))
       
       
'''       
mylist = []

for i in xrange(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
print mylist       
 

# Code Sample A <----DETERMINISTIC
mylist = []

for i in xrange(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        if number not in mylist:
            mylist.append(number)
print mylist

    
     
# Code Sample B <-----NOT DETERMINISTIC (STOCHIASTIC)
mylist = []

random.seed(0)
for i in xrange(random.randint(1, 10)):
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
    print mylist
'''
      
#testRandGen()