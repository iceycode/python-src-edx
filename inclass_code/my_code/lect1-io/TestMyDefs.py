'''
Created on Oct 21, 2014

@author: Allen
'''
import unittest
import sys

import lect1exs


class TestMyDefs(unittest.TestCase):
    

    def setUp(self):
        isItTrue1 = lect1exs.isAlphabeticalWord("awall") #no list
        


    def testName(self):
        self.assertEquals(self.isItTrue1, True)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    sys.argv = ['', 'TestMyDefs.']
    
    unittest.main()