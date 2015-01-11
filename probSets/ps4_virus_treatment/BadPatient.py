__author__ = 'Allen'
__doc__ = """
A subclass of TreatedPatient from ps3b
NOTE: for some reason, even though my problem set
 code was correct in ps3 (the previous lab); the
 plots do not seem to behave at all like they are supposed
 to.
 Instead of using my own classes (ps3b.py) I am using
 classes in the precompiled code that came with
 problem set 3.

 ALSO, precompiled code & its imports show as unresolved references in pycharm,
     However, they can still be used - simply ignore the error
"""

from ps3b_precompiled_27 import *




class BadPatient(TreatedPatient):
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
        TreatedPatient.__init__(self, viruses, maxPop)

    def addPrescription(self, newDrug):
        """
        this patient never takes the drug
        :param: newDrug: nothing actually done with this
        """
        #this patient will NEVER take the drug
        #nothing done here


    # def getPrescriptions(self):
    #     """
    #     Returns the drugs that are being administered to this patient.
    #     :returns: The list of drug names (strings) being administered to this
    #              patient.
    #     """
    #     return self.drugs
    #
    #
    # def getResistPop(self, drugResist):
    #     """
    #     Get the population of virus particles resistant to the drugs listed in
    #     drugResist.
    #
    #     :param: drugResist: Which drug resistances to include in the population (a list
    #                 of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])
    #
    #     :return: The population of viruses (an integer) with resistances to all
    #              drugs in the drugResist list.
    #     """
    #     resistViruses = 0
    #     for virus in self.getViruses():
    #         if virus.checkResistances(drugResist):
    #             resistViruses += 1
    #
    #     return resistViruses
    #
    # def removeViruses(self, viruses):
    #     """
    #     removes viruses from list if they die
    #     :param viruses: current list of viruses
    #     :return: updated list of viruses
    #     """
    #     for virus in viruses:
    #         #if virus dies off
    #         if virus.doesClear():
    #             viruses.remove(virus)
    #     self.viruses = viruses[:]
    #
    #
    # def virusReplication(self, viruses, activeDrugs, popDensity):
    #     """
    #     replicates viruses, setting new viruses
    #     :param viruses:
    #     :param activeDrugs
    #     :param popDensity
    #     """
    #     viruses_replicating = viruses[:]
    #     for virus in viruses_replicating:
    #         try:
    #             newVirus = virus.reproduce(popDensity, activeDrugs)
    #         except NoChildException:
    #             pass
    #         else:
    #             viruses.append(newVirus)
    #
    #     self.viruses = viruses[:]
    #
    # def update(self):
    #     """
    #     Update the state of the virus population in this patient for a single
    #     time step. update() should execute these actions in order:
    #
    #     - Determine whether each virus particle survives and update the list of
    #       virus particles accordingly
    #
    #     - The current population density is calculated. This population density
    #       value is used until the next call to update().
    #
    #     - Based on this value of population density, determine whether each
    #       virus particle should reproduce and add offspring virus particles to
    #       the list of viruses in this patient.
    #       The list of drugs being administered should be accounted for in the
    #       determination of whether each virus particle reproduces.
    #
    #     :returns: The total virus population at the end of the update (an
    #             integer)
    #     """
    #     #removes viruses & updates list in patient
    #     self.removeViruses(self.getViruses())
    #
    #     #after removals, calculate pop. density
    #     currPopDensity = self.getTotalPop()/self.getMaxPop()
    #
    #     self.virusReplication(self.getViruses(), self.getPrescriptions(), currPopDensity)
    #     return self.getTotalPop()


