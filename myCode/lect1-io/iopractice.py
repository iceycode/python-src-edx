''' practice for input/output 

Created on Oct 22, 2014

@author: Allen
'''

import pylab
import numpy as np


#method which extracts temperature data
def getFileInfo():
    inf = open('julyTemps.txt') #file being read
    
    hiTemps = []#list of high temps
    lowTemps = [] #list of low temps
    
    for line in inf:
        fields = line.split() #splits this line
        
        #if 'Boston'==fields[0] or '-'==fields[0] or 'Day'==fields[0] or ' ' == fields[0]:
        if len(fields)<3 or not fields[0].isdigit() :
            continue
        else :
            hiTemps.append(fields[1])
            lowTemps.append(fields[2])
 
    return (lowTemps, hiTemps)


#method that creates the plot
def producePlot(lowTemps, highTemps):
 
    diffTemps = list(np.array(highTemps) - np.array(lowTemps))
    #pylab.figure(1)
    pylab.plot(range(1,32), diffTemps) 
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.show()
    
    
(low, high) = getFileInfo()
producePlot(low, high)






'''ALT code

    #reads all the lines, this is shorter &
    # has advantage that properly closed even if exception raised
    with open('julyTemps.txt') as inf :
        #lines = inf.readlines() #this gives all lines, including blank ones
        lines = filter(None, (line.rstrip() for line in inf)) #strips the empty lines
        #inf.close()
    
    #my code for getting fields 
    fields = [line.split() for line in lines]

    for field in fields:
        if not field[0].isdigit():
            fields[1] += hiTemps
            fields[2] += lowTemps 
        if (field[0]=='Boston' or field[0]=='-' or field[0]=='Day'):
            print(field)
   
       diffTemps = [] #list of differences b/w high & low temps
    highTemps = temps[0] #y-coordinates
    lowTemps = temps[1] #x-coordinates
    #get the differnece in temperatures
    i = 0
    while i < 31 :
        diff = int(highTemps[i]) - int(lowTemps[i])
        diffTemps.append(diff)
        i+=1
        print(diff)
   
   
'''
 