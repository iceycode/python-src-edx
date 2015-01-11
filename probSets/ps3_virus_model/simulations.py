__author__ = 'Allen'

import pylab
from ps3b_precompiled_27 import *

#
# PROBLEM 5
#
# Enter your definition for simulationWithDrug in this box
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    :param: numViruses: number of ResistantVirus to create for patient (an integer)
    :param: maxPop: maximum virus population for patient (an integer)
    :param: maxBirthProb: Maximum reproduction probability (a float between 0-1)
    :param: clearProb: maximum clearance probability (a float between 0-1)
    :param: resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    :param: mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1).
    :param: numTrials: number of simulation runs to execute (an integer)
    """
    #random.seed(0) #for debugging purposes
    avgs_total1 = [0.0]*300 #for total virus population
    avgs_total2 = [0.0]*300 #for guttagonol-resistant virus pop.

    for trial in range(numTrials):
        #create the viruses
        viruses = []
        for v in range(numViruses):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))

        drug = 'guttagonol'
        drugList = [drug]
        patient = TreatedPatient(viruses, maxPop)
        #300 steps, pop. at time=0 corresponds to first update() call
        for t in range(300):
            avgs_total1[t] += patient.update()/float(numTrials)
            avgs_total2[t] += float(patient.getResistPop(drugList))/float(numTrials)
            if t == 149:
                patient.addPrescription(drug)

    plotWithDrugSimulation([i for i in xrange(300)], avgs_total1, avgs_total2)

import matplotlib.patches as mpatches
def plotWithDrugSimulation(time, avg_pops, avg_resist_pops):
    '''
    Plots averages of populations over number of trials as function of time
    :param xAxis:
    :param avg_pops:
    '''
    pylab.figure(1)
    pylab.plot(time, avg_pops, 'r',label = "Total Population")
    pylab.plot(time, avg_resist_pops, 'b',label = "Resistant Population")
    pylab.title("Simulation with drugs")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend()

    # fills between the 2 lines on graph
    # pylab.figure(1)
    # pylab.title("Simulation with drugs")
    # pylab.xlabel("Time Steps")
    # pylab.ylabel("Average Virus Population")
    # pylab.fill_between(time, avg_pops, 0, facecolor='blue')
    # pylab.fill_between(time, avg_resist_pops, 0, facecolor='red')
    # bp = mpatches.Patch(color='red', label='Drug-Resistant Population')
    # rp = mpatches.Patch(color='blue', label='Total Population')
    # pylab.legend(handles=[bp, rp])

    pylab.show()


simulationWithDrug(100, 20, 0.1, 0.05, {"guttagonol": False}, 0.5, 50)