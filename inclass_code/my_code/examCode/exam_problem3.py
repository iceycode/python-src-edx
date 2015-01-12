import random
import pylab

'''
Simulates Fox & rabbit population growth in forest
Max pop of rabbits determined by amt of vegetation in forest, which is relatively stable
  Never few than 10 rabbits, max pop is 1000
  For each rabbit, at each time step, probability = 1.0 - curr pop/max pop
For Fox, never fewer than 10 foxes (no max pop)
  At each tiem step, after rabbits done reproducing, fox hunts rabbit with success rate:
        p = current rabbit pop/max rabbit population
  If succeeds, pop rabbits decrease by 1; fox has, at that time step, 1/3 prob of reproducing
  If fails, 10% chance of dying at that time step

Start: 500 rabbits, 30 foxes; at end of time step, record foxes & rabbits

NOTE: do not define global variables: MAXRABBITPOP, CURRENTRABBITPOP, or CURRENTFOXPOP in grader
'''


# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    for rabbit in xrange(CURRENTRABBITPOP):
        pr = 1.0 - float(CURRENTRABBITPOP)/float(MAXRABBITPOP)
        if random.random() >= pr and CURRENTRABBITPOP < MAXRABBITPOP:
            CURRENTRABBITPOP += 1

            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    prob_reproducing = 1.0/3.0
    prob_death = 0.90
    for fox in xrange(CURRENTFOXPOP):
        prob_eat = float(CURRENTRABBITPOP)/float(MAXRABBITPOP)
        # if fox is able to eat
        if random.random() <= prob_eat and CURRENTRABBITPOP > 10:
            CURRENTRABBITPOP -= 1
            if random.random() <= prob_reproducing:
                CURRENTFOXPOP += 1
        else:
            # fox can die
            if random.random() <= prob_death and CURRENTFOXPOP > 10:
                CURRENTFOXPOP -= 1
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    foxes = [0]*numSteps
    rabbits = [0]*numSteps

    for step in xrange(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbits[step] += CURRENTRABBITPOP
        foxes[step] += CURRENTFOXPOP

    return (rabbits, foxes)

# plotting the curves for rabbit & fox populations
def test_simulation(numSteps):
    print CURRENTRABBITPOP
    pops = runSimulation(numSteps)

    rabbit_pops, fox_pops = pops
    plot_populations(rabbit_pops, fox_pops)
    plot_polyfit(rabbit_pops, fox_pops)


def plot_populations(rabbit_pops, fox_pops):
    # the regular plots
    pylab.figure(1)
    pylab.title('Population Growth of Foxes & Rabbits')
    pylab.plot(rabbit_pops, 'b', label = 'Rabbit pop')
    pylab.plot(fox_pops, 'r', label = 'Fox pops')
    pylab.xlabel('Time')
    pylab.ylabel('Population')
    pylab.legend()

    plot_polyfit(rabbit_pops, fox_pops)

    pylab.show()



def plot_polyfit(rabbit_pops, fox_pops):
    # coefficients of a 2nd degree polynomial for rabbit & fox curvev
    coeff2_rabbit = pylab.polyfit(range(len(rabbit_pops)), rabbit_pops, 2)
    coeff2_fox = pylab.polyfit(range(len(fox_pops)), fox_pops, 2)

    print 'Coefficient of 2nd Degree Polynomial RABBIT = ', coeff2_rabbit
    print 'Coefficient of 2nd Degree Polynomial FOX = ', coeff2_fox

    # polyfit plots, 2nd degree polynomial coefficients
    pylab.figure(2)
    pylab.title('2nd Degree Polynomial Values of Fox & Rabbit Populations')
    pylab.plot(pylab.polyval(coeff2_rabbit, range(len(rabbit_pops))), 'b', label = 'Polyfit Rabbit Plot')
    pylab.plot(pylab.polyval(coeff2_fox, range(len(fox_pops))), 'r', label = 'Polyfit Fox Plot')
    pylab.xlabel('Time')
    pylab.ylabel('Population')
    pylab.legend()

#test_simulation(200)
