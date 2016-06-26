__author__ = 'Allen'

'''
Examples of clustering used in unsupervised learning
Features of good clustering:
    high inter-cluster dissimilarity
    low intra-cluster dissimilarity

C = set of clusters
c = clusters
V = variance
For intracluster dissimilarity:
    V(c) = sum(mean(c) - x)^2 for values in cluster
    baddness(C) = sum(variances) for set of clusters
'''

def clusterVariance(cluster):
    var = 0.0
    mean = sum(cluster, 0)/len(cluster)
    for x in cluster:
        var += (mean - x)**2

    return var

def badnessClusters(cVars):
    return sum(cVars)

set = [-6, -6, -4, -4, 2, 2, 2]
def yieldStuff(set):
    for x in set:
        yield x
set = yieldStuff(set)
print len(set)

# c1 = [2, 2, -6, -6]
# c2 = [-4, -4, 2]
# C1 = [2, 2, 2]
# C2 = [-6, -6, -4, -4]

c1 = [2, 2]
c2 = [-6, -6]
c3 = [-4, -4]

v1 = clusterVariance(c1)
v2 = clusterVariance(c2)
v3 = clusterVariance(c3)
print "c1 variance: ", v1, ", c2 variance: ", v2

badness = badnessClusters([v1, v2, v3])
print "badness of clusters c1, c2 = ", badness