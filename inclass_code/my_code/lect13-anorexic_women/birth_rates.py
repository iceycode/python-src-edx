__author__ = 'Allen'
'''
Examining statistical fallacies from Lecture 13
Texas Sharpshooter Fallacy
 - shot first, paint targets around shot to give
   illusion of being accurate
In this study, it was concluded anorexic women more likely born in spring
    +13% more born b/w March & June, +30 more in June
    446 anorexic women studied/12 possible birth months = 37
    so, ~48 born in June
For 1000 trials:
    Prob of at least 48 births in June =  0.039
    Prob of at least 48 births in June =  0.042
    Prob of at least 48 births in June =  0.044
If purely by random, 4% chance; so 95% accurate

HOWEVER, they should have checked ALL the months,
  NOT run experiment than draw circle around
    a particular month

Prob of at least 48 births in some month =  0.424

This shows that any month has probability of 42%, which
 means that there is no statistical significance when it comes
 to higher birth chances in certain months for anorexic women.
'''
import random

# shows that above result happened purely by chance
def juneProb(numTrials):
    june48 = 0.0
    for trial in range(numTrials):
        june = 0.0
        for i in range(446):
            if random.randint(1,12) == 6:
                june += 1.0
        if june >= 48:
            june48 += 1
    jProb = str(june48/numTrials)
    print 'Prob of at least 48 births in June = ', jProb

#juneProb(1000)

def anyMonth(numTrials):
    anyMonth = 0.0
    for trial in range(numTrials):
        months = [0.0]*13
        for i in range(446):
            months[random.randint(1,12)]+=1
        if max(months) >= 48:
            anyMonth += 1
    aProb = str(anyMonth/numTrials)
    print 'Prob of at least 48 births in some month = ', aProb

anyMonth(1000)