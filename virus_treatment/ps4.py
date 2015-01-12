# 6.00.2x Problem Set 4
"""
NOTE: for some reason, even though my problem set
 code was correct in ps3 (the previous lab); the
 plots do not seem to behave at all like they are supposed
 to.
 Instead of using my own classes (ps3b.py) I am using
 classes in the precompiled code that came with
 problem set 3.
"""


#import numpy
import pylab
#from ps3b import *
from ps3b_precompiled_27 import *


#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    #x-axis: final total virus population; choose bins based on this
    #y-axis: number of trials belonging to each histogram bin

    :param numTrials: number of simulation runs to execute (an integer)
    """
    #numViruses = 100, maxPop = 1000, maxBirth = .1, maxClear = .05,
    #initialize list of viruses

    drug = 'guttagonol'
    bins = [35, 25, 15, 7]
    virusCount = 100
    resistances = {drug: False}

    viruses = createViruses(virusCount, 0.1, 0.05, resistances, 0.005)

    delayPops = [] #stores final total population for delays
    delayTitles = [] #stores titles
    delays = [300, 150, 75, 0] #the delays

    #loop through delay values
    for d in xrange(len(delays)):
        delayTitles.append(str(delays[d])) #for plot titles

        #final populations for trials stored in list
        delayPops.append(trialsFinalPopulations(numTrials, viruses, drug, delays[d]))

    getPercentages(delayPops, delays)
    plotPopHistograms(delayPops, delayTitles, bins)



def trialsFinalPopulations(numTrials, viruses, drug, delay):
    '''
    Returns final virus population list for 1 drug added at delay
    :param numTrials: number of trials
    :param viruses: virus list
    :param drug: drug to add
    :param delay: time at which drug is added
    :return: pops: list of total virus populations for trials
    '''
    timeSteps = 450
    pops = [] # the final total virus pop list for trial
    #loop through trials
    for trial in xrange(numTrials):
        patient = TreatedPatient(viruses, 1000)
        finalPop = 0
        #299 time steps (since last step outside loop)
        for t in xrange(timeSteps-1):
            #check delay condition
            if t == delay:
                patient.addPrescription(drug)
            patient.update() #update patient

        #the last update added final total virus pop list
        pops.append(patient.update())

    return pops


def createViruses(numViruses, birthProb, clearProb, resistances, mutProb):
    '''
    Creates & returns a list of viruses with length numViruses

    :param numViruses: number of viruses created
    :param birthProb: birth probability
    :param clearProb: probability of being cleared
    :param resistances: dictionary of drug resistances
    :param mutProb: mutation probability
    :return: viruses: list of viruses
    '''
    viruses = []
    for i in range(numViruses):
        viruses.append(ResistantVirus(birthProb, clearProb, resistances, mutProb))

    return viruses




#shows percentage of final pop viruses below 50 to rest
def getPercentages(delayPops, delays):
    i = 0
    for pops in delayPops:
        countLess50 = 0.0
        for pop in pops:
            if 0 <= pop <= 50:
                countLess50 += 1.0

        print delays[i],"\t", countLess50/len(pops)
        i += 1


def plotPopHistograms(delayPops, delayTitles, binArr):
    '''
    Plots populations after delays of varying step size

    :param delayPops:
    :param bins: default across all is at 10
    '''

    mainTitle = "Populations Across Trials: Treatment Delay "

    for i in range(len(delayPops)):
        title = mainTitle + str(delayTitles[i])
        pylab.figure()
        pylab.xlabel("Final Populations")
        pylab.ylabel("Number of Trials")
        pylab.title(title)
        pylab.hist(delayPops[i], bins = binArr[i])
    pylab.show()


'''
Ratios final population <= 50 for delays
  Trials: 100
  Delays:       Ratios:
  300           0.0
  150           0.03
  75            0.13
  0             1.0

  Trials: 500
  Delays:       Ratios:
  300           0.0
  150           0.04
  75            0.134
  0             1.0
'''

#TODO: run 1000 trials again (see why 0 delay shouldnt be uniform???)
#simulationDelayedTreatment(1000) #1000 trials, TAKES A WHILE
#simulationDelayedTreatment(500)   #500 trials also takes a while
#simulationDelayedTreatment(100)  #100 trials, not too much time
#simulationDelayedTreatment(1000) #for testing, just 10 trials (W VARYING PARAMETERS)2








#################################################
#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    resistances = {'guttagonol': False, 'grimpex': False}
    drugs = ["guttagonol", "grimpex"]
    bins = [35, 25, 15, 15]
    virusCount = 100

    viruses = createViruses(virusCount, .1, .05, resistances, .5)

    delayPops = [] #stores final total population for delays
    delayTitles = [] #stores titles
    delays2 = [300, 150, 75, 0] #the delays

    #loop through delay values
    for d in xrange(len(delays2)):
        delayTitles.append(str(delays2[d])) #for plot titles

        #final populations for trials stored in list
        delayPops.append(trialFinalPops2Drugs(numTrials, viruses, drugs, delays2[d]))

    getPercentages(delayPops, delays2)
    plotPopHistograms(delayPops, delayTitles, bins)
    #plotWithSubplots(delayPops, delayTitles, delays2)



def trialFinalPops2Drugs(numTrials, viruses, drugs, delay, timeSteps = 450):
    '''
    Number of trials represents number of patients
    :param numTrials: number of trials
    :param timesteps: number of timesteps
    :param viruses: list of viruses
    :param drugs: list of drugs to administer
    :param delay: delay before administering 2nd drug
    :return: final populations
    '''
    admin1 = 150
    admin2 = admin1 + delay
    pops = [] # the final total virus pop list for trial

    #loop through trials
    for trial in xrange(numTrials):
        patient = TreatedPatient(viruses, 1000)
        finalPop = 0
        #299 time steps (since last step outside loop)
        for t in xrange(timeSteps - 1):
            if t == admin1:
                patient.addPrescription(drugs[0])

            #check delay condition
            if t == admin2:
                patient.addPrescription(drugs[1])
            patient.update() #update patient

        #the last update added final total virus pop list
        pops.append(patient.update())

    return pops


def plotWithSubplots(delayPops, delayTitles, delays):
    '''
    Plots populations after delays of varying step size

    :param delayPops:
    :param bins: default across all is at 10
    '''

    mainTitle = "Populations Across Trials: Treatment Delay "

    for i in range(len(delayPops)):
        title = mainTitle + str(delayTitles[i])
        pylab.figure(i)
        pylab.xlabel("Final Populations")
        pylab.ylabel("Number of Trials")
        pylab.title(title)

        subplot1 = [j <= 150 for j in delayPops[i]]
        subplot2 = [j > 150 for j in delayPops[i]]

        pylab.subplot(subplot1)
        pylab.plot(delayPops[i])
        pylab.subplot(subplot2)

    pylab.show()


'''
After 150 Steps, 1st drug given; 2nd drug after delay
Number of Trials: 10
Delays:     Ratio 0-50: 50-other
300 	    0.0
150 	    0.1
75 	        0.7
0 	        0.9

Number of Trials: 1000
Delays:     Ratio 0-50:50-other
300 	    0.035
150 	    0.117
75 	        0.482
0 	        0.836


Number of Trials: 50
Delays:     Ratio 0-50:50-other

'''
#2 drugs, 1st delayed by 150 steps, 2nd varying steps
# simulationTwoDrugsDelayedTreatment(1000)
# simulationTwoDrugsDelayedTreatment(5)
# simulationTwoDrugsDelayedTreatment(500)







"""
These are my own trials since I am curious as to the outcome of
 having a certain percentage of patients never taking the drug
"""

class BadPatient(TreatedPatient):
    """
    Subtype of TreatedPatient class
    Representation of a BAD treated patient.w
    The patient consciously or subconsiously forgets to take the drug
      or is unable to.
    """
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).

        :param: viruses: The list representing the virus population (a list of
                    virus instances)
8
        :param: maxPop: The  maximum virus population for this patient (an integer)
        """
        TreatedPatient.__init__(self, viruses, maxPop)

    def addPrescription(self, newDrug):
        """
        this patient never takes the drug
        :param: newDrug: nothing actually done with this
        """
        #this patient will NEVER take the drug
        #nothing done here

#import random

#1 delay & 1 drug with a certain percentage of patients
#  who never take the drug
def simulationWithBadPatients_1(numTrials, probNever):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    #x-axis: final total virus population; choose bins based on this
    #y-axis: number of trials belonging to each histogram bin

    :param numTrials: number of simulation runs to execute (an integer)
    :param percentNever: percetnage of patients that will not take the drug
    """
    #numViruses = 100, maxPop = 1000, maxBirth = .1, maxClear = .05,
    #initialize list of viruses

    drug = 'guttagonol'
    bins = [35, 25, 15, 7]
    virusCount = 100
    resistances = {drug: False}

    viruses = createViruses(virusCount, 0.1, 0.05, resistances, 0.005)

    delayPops = [] #stores final total population for delays
    delayTitles = [] #stores titles
    delays = [300, 150, 75, 0] #the delays

    #loop through delay values
    for d in xrange(len(delays)):
        delayTitles.append(str(delays[d])) #for plot titles

        #final populations for trials stored in list
        delayPops.append(trialsWithBadPatients(numTrials, viruses, drug, delays[d], probNever))

    getPercentages(delayPops, delays)
    plotPopHistograms(delayPops, delayTitles, bins)


def trialsWithBadPatients(numTrials, viruses, drug, delay, probNever):
    '''
    Returns final virus population list for 1 drug added at delay
    :param numTrials: number of trials
    :param viruses: virus list
    :param drug: drug to add
    :param delay: time at which drug is added
    :return: pops: list of total virus populations for trials
    '''
    timeSteps = 450
    pops = [] # the final total virus pop list for trial

    badpatientTrials = int(numTrials*probNever)
    normalTrials = numTrials - badpatientTrials


    #loop through trials
    for trial in xrange(normalTrials):
        patient = TreatedPatient(viruses, 1000)
        #299 time steps (since last step outside loop)
        for t in xrange(timeSteps-1):
            #check delay condition
            if t == delay:
                patient.addPrescription(drug)
            patient.update() #update patient

        #the last update added final total virus pop list
        pops.append(patient.update())

    for trial in xrange(badpatientTrials):
        badpatient = BadPatient(viruses, 1000)

        for t in xrange(timeSteps-1):
            #check delay condition
            if t == delay:
                badpatient.addPrescription(drug)
            badpatient.update() #update patient

        pops.append(badpatient.update())

    return pops


'''
Table of virus cured or not:
Trials: 50
Delays     Ratios (<50: over 50 virus count)
300 	   0.02
150 	   0.04
75 	       0.12
0 	       0.8

Trials: 500
Delays     Ratios: 20% bad      Ratios: Normal (all take drug - from previous sim)
300 	   0.014                0.0
150 	   0.03                 0.04
75 	       0.086                0.134
0 	       0.8                  0.86


'''

#simulationWithBadPatients_1(50, .2) #only 50 trials & 20% bad patients
simulationWithBadPatients_1(500, .2) #simulation with 500 trials with 20% bad patients