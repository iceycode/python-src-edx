# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

#import numpy
import random
import pylab

#### NOTE: this seems to be missing
## from psb3_precompiled_27 import *

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 2
#
class SimpleVirus(object):
    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.
        :param: maxBirthProb: Maximum reproduction probability (a float between 0-1)
        :param: clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        :returns: Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        :return: Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """
        Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step.
        :return: True if probability under self.getClearProb, otherwise returns False.
        """
        if random.random() <= self.getClearProb():
            return True
        return False

    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).

        :param: popDensity the population density (a float), defined as the current
                virus population divided by the maximum population.
        :returns: a new instance of the SimpleVirus class representing the
                offspring of this virus particle. The child should have the same
                maxBirthProb and clearProb values as this virus. Raises a
        :exception: NoChildException if this virus particle does not reproduce.
        """
        reprProb = self.getMaxBirthProb() * (1 - popDensity)
        try:
            assert(random.random() <= reprProb)
        except:
            #return None
            raise NoChildException
        else:
            return SimpleVirus(reprProb, self.getClearProb())



class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        :param: viruses: the list representing the virus population
                (a list of SimpleVirus instances)
        :param: maxPop: the maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop

    def setViruses(self, viruses):
        """
        sets viruses
        :param viruses:
        """
        self.viruses = viruses

    def getViruses(self):
        """
        :return: the viruses in this Patient.
        """
        return self.viruses

    def getMaxPop(self):
        """
        :return: the max population.
        """
        return self.maxPop

    def getTotalPop(self):
        """
        Gets the size of the current total virus population.
        :return: The total virus population (an integer)
        """
        return len(self.getViruses())

    def removeViruses(self, viruses):
        """
        removes viruses from list if they die
        :param viruses: current list of viruses
        :return: updated list of viruses
        """
        for virus in viruses:
            #if virus dies off
            if virus.doesClear():
                viruses.remove(virus)
        self.setViruses(viruses)

    def virusReplication(self, viruses, popDensity):
        """
        replicates viruses
        :param viruses:
        """
        viruses_replicating = list(viruses)
        for virus in viruses_replicating:
            try:
                newVirus = virus.reproduce(popDensity)
            except NoChildException:
                pass
            else:
                viruses.append(newVirus)

        self.setViruses(viruses)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        - Determine whether each virus particle survives and updates the list
          of virus particles accordingly.

        - The current population density is calculated. This population density
          value is used until the next call to update()

        - Based on this value of population density, determine whether each
          virus particle should reproduce and add offspring virus particles to
          the list of viruses in this patient.

        :return: The total virus population at the end of the update (an integer)
        """
        #removes viruses & updates list in patient
        self.removeViruses(self.getViruses())

        #after removals, calculate pop. density
        currPopDensity = self.getTotalPop()/self.getMaxPop()

        self.virusReplication(self.getViruses(), currPopDensity)

        return self.getTotalPop()



#
# PROBLEM 3
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).
    For each of numTrials trial, instantiates a patient, runs a simulation for 300 timesteps,
    and plots the average virus population size as a function of time.

    :param: numViruses: number of SimpleVirus to create for patient (an integer)
    :param: maxPop: maximum virus population for patient (an integer)
    :param: maxBirthProb: Maximum reproduction probability (a float between 0-1)
    :param: clearProb: Maximum clearance probability (a float between 0-1)
    :param: numTrials: number of simulation runs to execute (an integer)
    """
    #random.seed(0) #for debugging purposes
    avgs_total = [0]*300 #initialize virus pop totals list

    for trial in range(numTrials):
        #create the viruses
        viruses = [] #stores viruses (new for each trial)
        for virus in range(numViruses):
            viruses.append(SimpleVirus(maxBirthProb, clearProb))

        patient = Patient(viruses, maxPop)
        #pops = [] #keeps averages for each virus
        #300 steps, pop. at time=0 corresponds to first update() call
        for t in range(300):
            currPop = patient.update()
            avgs_total[t] += currPop


    #average calculation at each time step
    avg_pops = []
    xAxis = []
    for i in range(300):
        avg_pops.append(float(avgs_total[i]/numTrials))
        xAxis.append(i)

    #print "Plotting averages during time steps = ", avg_pops

    plotWithoutDrugSimulation(xAxis, avg_pops)


def plotWithoutDrugSimulation(xAxis, avg_pops):
    '''
    Plots averages of populations over number of trials as function of time
    :param xAxis:
    :param avg_pops:
    '''
    pylab.plot(xAxis, avg_pops)
    pylab.figure()
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend('SimpleVirus')
    pylab.show()

# def setupPlot():
#     #set line width
#     pylab.rcParams['lines.linewidth'] = 3
#     #set font size for titles
#     pylab.rcParams['axes.titlesize'] = 20
#     #set font size for labels on axes
#     pylab.rcParams['axes.labelsize'] = 15
#     #set size of numbers on x-axis
#     pylab.rcParams['xtick.major.size'] = 5
#     #set size of numbers on y-axis
#     pylab.rcParams['ytick.major.size'] = 5

#numVirsues=100, maxPop = 1000, maxBirthProb = .1, clearProb = .05; numTrials = 100
#simulationWithoutDrug(1, 10, 1.0, 0.0, 1)
#simulationWithoutDrug(1, 90, 0.8, 0.1, 1)
#simulationWithoutDrug(100, 200, 0.2, 0.8, 1)
#simulationWithoutDrug(100, 1000, 0.1, .05, 100)

#
# PROBLEM 4
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        :param: maxBirthProb: Maximum reproduction probability (a float between 0-1)
        :param: clearProb: Maximum clearance probability (a float between 0-1).
        :param: resistances: A dictionary of drug names (strings) mapping to the state
                of this virus particle's resistance (either True or False) to each drug.
                e.g. {'guttagonol':False, 'srinol':False}, means that this virus
                particle is resistant to neither guttagonol nor srinol.
        :param: mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistances(self):
        """
        :return: the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        :return: the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        :param: drug: The drug (a string)
        :returns: True if this virus instance is resistant to the drug, False otherwise.
        """
        if drug not in self.getResistances().keys():
            #if not in list, assume virus is NOT resistant (return false) assume no reproduction
            return False
        else:
            return self.getResistances()[drug]

    def checkResistances(self, activeDrugs):
        for drug in activeDrugs:
            if not self.isResistantTo(drug):
                return False
        return True

    def childResistances(self):
        mutProb_inherit = 1.0 - self.getMutProb()
        for k, v in self.getResistances().iteritems():
            cres_mutProb = random.random() #stochiastically determines inheritance
            if self.getMutProb() < cres_mutProb <= mutProb_inherit:
                self.getResistances()[k] = v
            elif cres_mutProb <= self.getMutProb():
                self.getResistances()[k] = not v
        return self.getResistances()


    def canReplicate(self, popDensity):
        if random.random() <= self.getMaxBirthProb() * (1.0 - popDensity):
            return True
        return False


    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.
        Hence, if the virus is resistant to all drugs in activeDrugs,
        then the virus reproduces with probability: self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb & clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.

        :param: popDensity: the population density (a float), defined as the current
                virus population divided by the maximum population

        :param: activeDrugs a list of the drug names acting on this virus particle (a list of strings).

        :returns: a new instance of the ResistantVirus class representing the
                offspring of this virus particle. The child should have the same
                maxBirthProb and clearProb values as this virus. Raises a
                NoChildException if this virus particle does not reproduce.
        """
        try:
            assert(self.checkResistances(activeDrugs))
            assert(self.canReplicate(popDensity, activeDrugs))

        except Exception, e:
            raise NoChildException(e)
        else:
            return ResistantVirus(self.getMaxBirthProb(), self.getClearProb(), self.childResistances(), self.getMutProb())




class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
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
        Patient.__init__(self, viruses, maxPop)
        self.drugs = [] #initialize list of drugs as empty


    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        :param: newDrug: The name of the drug to administer to the patient (a string).

        :param: postcondition: The list of drugs being administered to a patient is updated
        """
        if newDrug not in self.getPrescriptions():
            self.getPrescriptions().append(newDrug)

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.
        :returns: The list of drug names (strings) being administered to this
                 patient.
        """
        return self.drugs


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        :param: drugResist: Which drug resistances to include in the population (a list
                    of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        :return: The population of viruses (an integer) with resistances to all
                 drugs in the drugResist list.
        """
        resistViruses = 0
        for virus in self.getViruses():
            if virus.checkResistances(drugResist):
                resistViruses += 1

        return resistViruses

    def removeViruses(self, viruses):
        """
        removes viruses from list if they die
        :param viruses: current list of viruses
        :return: updated list of viruses
        """
        for virus in viruses:
            #if virus dies off
            if virus.doesClear():
                viruses.remove(virus)
        self.viruses = viruses[:]


    def virusReplication(self, viruses, activeDrugs, popDensity):
        """
        replicates viruses, setting new viruses
        :param viruses:
        :param activeDrugs
        :param popDensity
        """
        viruses_replicating = viruses[:]
        for virus in viruses_replicating:
            try:
                newVirus = virus.reproduce(popDensity, activeDrugs)
            except NoChildException:
                pass
            else:
                viruses.append(newVirus)

        self.viruses = viruses[:]

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        :returns: The total virus population at the end of the update (an
                integer)
        """
        #removes viruses & updates list in patient
        self.removeViruses(self.getViruses())

        #after removals, calculate pop. density
        currPopDensity = self.getTotalPop()/self.getMaxPop()

        self.virusReplication(self.getViruses(), self.getPrescriptions(), currPopDensity)

        return self.getTotalPop()


#
# PROBLEM 5
#
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
            avgs_total1[t] += patient.update()
            avgs_total2[t] += patient.getResistPop(drugList)
            if t == 149:
                patient.addPrescription(drug)

    #average calculation at each time step
    avg_pops = [0.0]*300
    avg_resist_pops = [0.0]*300
    xAxis = [0]*300
    for i in range(300):
        avg_pops[i] = float(avgs_total1[i])/float(numTrials)
        avg_resist_pops[i] = float(avgs_total2[i])/float(numTrials)
        xAxis[i] = i

    plotWithDrugSimulation(xAxis, avg_pops, avg_resist_pops)


def plotWithDrugSimulation(xAxis, avg_pops, avg_resist_pops):
    '''
    Plots averages of populations over number of trials as function of time
    :param xAxis:
    :param avg_pops:
    '''
    pylab.plot(xAxis, avg_pops, label = "Total Population")
    pylab.plot(xAxis, avg_resist_pops, label = "Resistant Population")
    pylab.title("Simulation with drugs")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend()
    pylab.figure(1)
    pylab.show()

#numViruses = 100, maxPop = 1000, maxBirth = .1, maxClear = .05,
mutProb = .05
resistances = {'guttagonol': False}
numTrials = 30
simulationWithDrug(100, 1000, .7, .05, {'guttagonol': False}, .05, 5)
#simulationWithDrug(1, 10, 1.0, 0.0,{}, 1.0, 5)
#simulationWithDrug(1, 20, 1.0, 0.0, {"guttagonol": True}, 1.0, 5)
#simulationWithDrug(1, 20, 1.0, 0.0, {"guttagonol": True}, 1.0, 5)