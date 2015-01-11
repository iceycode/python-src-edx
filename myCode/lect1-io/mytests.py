'''
My tests for the functions in lect1exs.py

Created on Oct 21, 2014

@author: Allen
'''


from lect1exs import isAlphabeticalWord, lotsOfParameters1, lotsOfParameters2, lotsOfParameters3
from lect1.lect1exs import lotsOfParameters3

#tests here
testWL1 = ["zombie", "gas", "elf", "box"]

val = isAlphabeticalWord("abcd")
print("Default, alphabetical string, should be true " + str(val))

val = isAlphabeticalWord("zap")
print("Default, word with non-alphabetical letters, should be false " + str(val) )

isAlphabeticalWord("gas", testWL1)
print("User variable, list with word in it but not alphabetical, should be false " + str(val) )

val = isAlphabeticalWord('box', testWL1)
print("User variable, word alphabetical & list contains it, should be true " + str(val))



#now tests for second problem
#lotsOfParameters1() #SyntaxError: needs to take in 5 arguments
#lotsOfParameters1(1, 2) # see above
#lotsOfParameters1(a=5,b=1,c=4,d=2,3) #SyntaxError: non-keyword arg after keyword arg
#lotsOfParameters1(e=5,d=4,c=3,b=2,1) #SyntaxError: non-keyword arg after keyword arg

#lotsOfParameters1(1,2,3,4,5) #WORKS
lotsOfParameters1(e=5,a=1,d=4,b=2,c=3) #WORKS
lotsOfParameters1(1,e=5,d=4,c=3,b=2) #WORKS
lotsOfParameters1(e=5,a=1,d=4,b=2,c=3)

''' for the default variables in 
'''
lotsOfParameters2(1, e=20, b=3) #WORKS
#lotsOfParameters2(1, e=20, b=3, a = 10)#TypeError: lotsOfParameters2() got multiple values for keyword argument 'a'

lotsOfParameters3(1, c=3) #TypeError: lotsOfParameters3() takes at least 2 arguments (2 given)

