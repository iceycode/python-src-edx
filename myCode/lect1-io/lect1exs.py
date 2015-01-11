'''
Exercises from lecture 1
L1.1 : default value exercise
L1.2 : keyword assignments
L1.3 : ... 

Created on Oct 21, 2014

@author: Allen
'''


#From lecture 1, problem 1
'''
Returns true if word is alphabetical order & false if not
 Also, if word list is provided & not a word, then false
  else, would show as true
make it so that a default value for wordList is given
- if user gives a list of words to check against
    they should 

NOTE: don't use mutable as default, as they will always change assignment

def given in problem 1
'''
def isAlphabeticalWord(word, wordList = None):
    if (len(word) > 0):
        curr = word[0]
    for letter in word : 
        if (curr > letter):
            return False
        else:
            curr = letter
    if wordList is None :
        return True
    return word in wordList
        
        
''' Problem set 2, question 1
def given in problem 2
using non-default variables
'''
def lotsOfParameters1(a,b,c,d,e):
    print a
    print b
    print c
    print d
    print e



''' Problem set 2, Question 2

using default variables

'''
def lotsOfParameters2(a=1,b=2,c=3,d=4,e=5):
    print a
    print b
    print c
    print d
    print e


'''Problem set 2, Question 3
last 3 are defaults, first 2 are not
'''
def lotsOfParameters3(a,b,c=3,d=4,e=5):
    print a
    print b
    print c
    print d
    print e



