__author__ = 'Allen'

## precompiled reference
from ps3b import *

'''for testing SimpleVirus/Patient classes'''

def initiate_class_test():
    random.seed()
    ## virus that always reproduces and always cleared
    viruses1 = [SimpleVirus(1.0, 0.0)]
    print "Patient test 1; clearPro = 0, maxBirthProb = 1.0"
    patient_test(viruses1)

    #virus that always reproduces and always cleared
    viruses2 = [SimpleVirus(1.0, 1.0)]
    print "Patient test 2; clearPro = 1.0, maxBirthProb = 1.0"
    patient_test(viruses2, 1)

    #virus with probMaxBirth = .96, clear = .12
    #testing random virus
    print "testing virus with clearProb = .96 & maxBirthProb = .12"
    virus_test(.96, .12)

    print "testing virus that has clearPro = 0.0 & maxBirthProb = 0.0"
    virus_test(0.0, 0.0)

    print "testing virus that has clearPro = 1.0 & maxBirthProb = 0.0"
    virus_test(1.0, 0.0)

    ## ResistantVirus Tests
    ##   is never cleared always reproduces
    resistantVirusTest( 1.0, 0.0, {}, 0.0)


def virus_test(clearProb, maxBirthProb):
    '''
    testing simple virus
    :param clearProb:
    :param maxBirthProb:
    '''
    virus = SimpleVirus(maxBirthProb, clearProb)
    popDensity = .04
    for i in range(10):
        try:
            virus.reproduce(popDensity)
        except:
            print "raised a NoChildException"
        else:
            print "Virus did reproduce"

def patient_test(viruses, maxPop=100, numTrials=1):
    '''
    tests patient class (numTrials equivalent to time steps)
    :param viruses:
    :param maxPop: default is 100
    :param numTrials: default is 100
    '''
    for trial in range(numTrials):
        #viruses_trial = viruses #init viruses for trial
        patient = Patient(viruses, maxPop)
        for step in range(1,100):
            totalPop = patient.update()
        print "virus amount = ", totalPop



def resistantVirusTest(ResistantVirus):
    '''
    testing simple virus
    '''
    # virus = ResistantVirus(1.0, 0.0, {"drug1":True, "drug2":False}, 0.0)
    # popDensity = .04

    # for i in range(10):
    #     try:
    #         virus.reproduce(popDensity, ["drug1"])
    #         virus.reproduce(popDensity, ["drug1"])
    #         virus.reproduce(popDensity, ["drug2"])
    #     except:
    #         print "raised a NoChildException"
    #     else:
    #         print "Virus did reproduce"


    totalRes = 0
    changedRes = 0.0
    for i in range(10):
        try:
            virus = virus.reproduce(0, [])
        except Exception:
            raise NoChildException
        print "test getting items ", virus.getResistances()

    print "total that changed resistances = ", changedRes, " virus res: ", virus.getResistances()


#initiate_class_test()
# drugDict = {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}
# res_virus = ResistantVirus(1.0, 0.0, drugDict, 0.5)
# resistantVirusTest(res_virus)


def res_virus_Test_Reproduction():
    '''
    testing simple virus
    :param ResistantVirus:
    '''

    # virus = ResistantVirus(1.0, 0.0, {"drug1":True, "drug2":False}, 0.0)
    # print virus.isResistantTo("drug1")
    # virus = ResistantVirus(1.0, 0.0, {"drug1":True, "drug2":False}, 0.0)
    # print "Test: ", virus.reproduce(0, ["drug2"])
    # print "Test: ", virus.reproduce(0, ["drug1"])

    #testing to see that at least half the drug resistances of children are not changed (since .5 mutProb)
    # drugDict = {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}
    # virus = ResistantVirus(1.0, 0.0, drugDict, 0.5)
    # changes = [] #keeps track of changes in virus
    # for i in range(10):
    #     try:
    #         child_virus = virus.reproduce(0, [])
    #     except Exception:
    #         raise NoChildException
    #     print "test getting items ", child_virus.getResistances()
    #
    #     curr_drugDict = child_virus.getResistances()
    #     for k, v in curr_drugDict.iteritems():
    #         if v != drugDict[k]:
    #             changes.append(1.0)
    #
    # print "total changes in child.getResistances() = ", changes
    #to check drug resists arent changed when adding to non-reproducing virus
    #virus = ResistantVirus(0.0, 1.0, {"drug1":True, "drug2":False}, 0.0)
    #virus.reproduce(0.0, [])
    #print "testing to make sure values not changed", virus.getResistances()

    #check for virus reproduction; drug2 is false, so should not reproduce
    #virus1 = ResistantVirus(0.0, 0.0, {"drug1":True, "drug2":False}, 0.0)
    virus2 = ResistantVirus(0.0, 0.0, {"drug1":True, "drug2":False}, 0.0)

    try:
        print "Test reproduce2 :", virus2.reproduce(0, ["drug1"]) #should NOT reproduce
        print "Test reproduce1 : ", virus2.reproduce(0, ["drug1"]) #should reproduce
    except NoChildException:
        print "Test: virus did NOT reproduce", virus2
        pass


def test_treatedPatient(resViruses, maxPop, numTrials=1):
    # for trial in range(numTrials):
    #
    #     patient = TreatedPatient(resViruses, maxPop)
    #     #pops = [] #keeps averages for each virus
    #     #300 steps, pop. at time=0 corresponds to first update() call
    #     for t in range(300):
    #         currPop = patient.update()
    #         print "curr population ", currPop
    #         print "drugs added = "
    patient = TreatedPatient(resViruses, maxPop)
    print patient.getResistPop(['drug1']) # should be 2
    print patient.getResistPop(['drug2']) #should be 2
    print patient.getResistPop(['drug1','drug2']) #should be 1
    print patient.getResistPop(['drug3']) # should be 0
    print patient.getResistPop(['drug1', 'drug3']) # should be 0
    print patient.getResistPop(['drug1','drug2', 'drug3']) # should be 0


#res_virus_Test_Reproduction()
virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
virus2 = ResistantVirus(1.0, 0.0, {"drug1": False, "drug2": True}, 0.0)
virus3 = ResistantVirus(1.0, 0.0, {"drug1": True, "drug2": True}, 0.0)
test_treatedPatient([virus1, virus2, virus3], 100)