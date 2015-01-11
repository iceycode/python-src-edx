import random

def strToInt(s):
    number = ''
    for c in s:
        number = number + str(ord(c))
    index = int(number)
    return index

#print 'Index =', strToInt('a')

#Very long number; do we really want a number that long in list?
#print 'Index =', strToInt('John is a cool dude')


'''
This hash function ensures number list is no
bigger than 100
'''
def hashStr(s, tableSize = 101):
    number = ''
    for c in s:
        number = number + str(ord(c))
    index = int(number)%tableSize
    return index

#ensures strings are not very long numbers
print 'Index  = ', hashStr('a')
print 'Index  = ', hashStr('John is a cool dude')

#hash Eric,
print hashStr('Eric', 7)
print hashStr('Chris', 7)
print hashStr('Sarina', 7)

#Jill also hashes to Sarina's index
print hashStr('Jill', 7)

