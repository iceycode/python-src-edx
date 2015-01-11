import pylab
'''
Looking at 100 patients with 4 features
cardiac health being assessed

Scaled Test Results:
original values [23, 25, 28, 21, 24, 24, 29, 26, 25, 29]

scaled values [-0.96076892 -0.16012815  1.040833   -1.76140969 -0.56044854 -0.56044854
  1.44115338  0.24019223 -0.16012815  1.44115338]

new mean =  5.55111512313e-16

new sd =  1.0
'''
import random

def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def scaleFeatures(vals):
    vals = pylab.array(vals)
    mean = sum(vals)/float(len(vals))
    sd = stdDev(vals)
    vals = vals - mean
    return vals/sd



def testScaling(n,mean,std):
    vals = []
    for i in range(n):
        vals.append(int(random.gauss(mean,std)))
    print 'original values', vals
    sVals = scaleFeatures(vals)
    print '\n','scaled values',sVals
    print '\n','new mean = ', sum(sVals/len(vals))
    print '\n','new sd = ', stdDev(sVals)
    
testScaling(10,25,3)