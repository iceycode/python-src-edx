#Code shared across examples
import pylab, string, random

def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

# scales all the features by getting rid of variance
# among the features
def scaleFeatures(vals):
    """Assumes vals is a sequence of numbers"""
    result = pylab.array(vals)
    mean = sum(result)/float(len(result))
    result = result - mean
    sd = stdDev(result)
    result = result/sd
    return result

class Point(object):

    def __init__(self, name, originalAttrs):
        """originalAttrs is an array"""
        self.name = name
        self.attrs = originalAttrs

    def dimensionality(self):
        return len(self.attrs)

    def getAttrs(self):
        return self.attrs

    def distance(self, other):
        #Euclidean distance metric
        result = 0.0
        for i in range(self.dimensionality()):
            result += (self.attrs[i] - other.attrs[i])**2
        return result**0.5

    def getName(self):
        return self.name

    def toStr(self):
        return self.name + str(self.attrs)

    def __str__(self):
        return self.name        
    
class Cluster(object):
    """ A Cluster is defines as a set of elements, all having 
    a particular type """
    def __init__(self, points, pointType):
        """ Elements of a cluster are saved in self.points
        and the pointType is also saved
        :param list of point objects
        :param pointType: the type of point (ie City)
        """
        self.points = points
        self.pointType = pointType

    def singleLinkageDist(self, other):
        """ Returns the float distance between the points that 
        are closest to each other, where one point is from 
        self and the other point is from other. Uses the 
        Euclidean dist between 2 points, defined in Point.
        :param other cluster
        :return distance of points that are closest to each other
        """
        if len(self.points) > len(other.points):
            members1 = self.points
            members2 = other.points
        else:
            members1 = other.points
            members2 = self.points
        smallestDist = -1 #initialize closest

        for p in members1:
            for op in members2:
                temp = p.distance(op)
                if smallestDist < 0:
                    smallestDist = temp
                elif temp < smallestDist:
                    smallestDist = temp

        return smallestDist

    def maxLinkageDist(self, other):
        """ Returns the float distance between the points that 
        are farthest from each other, where one point is from 
        self and the other point is from other. Uses the 
        Euclidean dist between 2 points, defined in Point.
        :param other
        :return distance between points that are farthest from each other
        """
        if len(self.points) > len(other.points):
            members1 = self.points
            members2 = other.points
        else:
            members1 = other.points
            members2 = self.points

        largestDist = -1 #initialize closest
        for p in members1:
            for op in members2:
                temp = p.distance(op)
                if largestDist < 0:
                    largestDist = temp
                elif temp > largestDist:
                    largestDist = temp

        return largestDist

    def averageLinkageDist(self, other):
        """ Returns the float average (mean) distance between all 
        pairs of points, where one point is from self and the 
        other point is from other. Uses the Euclidean dist 
        between 2 points, defined in Point.
        :param other: other cluster being compared to
        :return average distance b/w all pairs of points
        """
        totalDist = 0.0
        if len(self.points) > len(other.points):
            members1 = self.points
            members2 = other.points
        else:
            members1 = other.points
            members2 = self.points

        for p in members1:
            for op in members2:
                totalDist += p.distance(op)

        return totalDist/(len(members1)+len(members2))

    def mysteryLinkageDist(self, other):
        av_dist = self.averageLinkageDist(other)
        max_dist = self.maxLinkageDist(other)
        min_dist = self.singleLinkageDist(other)
        retDist = 0.0

        if av_dist == max_dist and max_dist == min_dist:
            retDist = av_dist
        elif av_dist == max_dist:
            retDist = av_dist
        elif av_dist == min_dist:
            retDist = av_dist
        elif max_dist == min_dist:
            retDist = min_dist
        else:
            retDist = random.choice([av_dist,min_dist,max_dist])

        return retDist


    def members(self):
        """
        :return: list of points in this cluster
        """
        for p in self.points:
            yield p

    def isIn(self, name):
        """ Returns True is the element named name is in the cluster
        and False otherwise
        :param name: name of point in points
        """
        for p in self.points:
            if p.getName() == name:
                return True
        return False

    def toStr(self):
        """
        :return: clusters as string
        """
        result = ''
        for p in self.points:
            result = result + p.toStr() + ', '
        return result[:-2]

    def getNames(self):
        """ For consistency, returns a sorted list of all 
        elements in the cluster
        :return names of points as sorted list
        """
        names = []
        for p in self.points:
            names.append(p.getName())
        return sorted(names)

    def __str__(self):
        names = self.getNames()
        result = ''
        for p in names:
            result = result + p + ', '
        return result[:-2]

class ClusterSet(object):
    """ A ClusterSet is defined as a list of clusters """
    def __init__(self, pointType):
        """ Initialize an empty set, without any clusters
        :param pointType: type of point (ie City) """
        self.members = []

    def add(self, c):
        """ Append a cluster to the end of the cluster list
        only if it doesn't already exist. If it is already in the 
        cluster set, raise a ValueError
        :param c
        """
        if c in self.members:
            raise ValueError
        self.members.append(c)


    def getClusters(self):
        return self.members[:]


    def mergeClusters(self, c1, c2):
        """ Assumes clusters c1 and c2 are in self
        Adds to self a cluster containing the union of c1 and c2
        and removes c1 and c2 from self
        :param c1 : 1st cluster that will be merged
        :param c2 : 2nd cluster that will be merged """
        pointType = c1.pointType
        mergedPoints = [p for p in c1.points] + [p for p in c2.points]

        #append & remove clusters
        if c1 in self.members:
            self.members.remove(c1)
        if c2 in self.members:
            self.members.remove(c2)
        self.members.append(Cluster(mergedPoints, pointType))


    def findClosest(self, linkage):
        """ Returns a tuple containing the two most similar
         clusters in self. No matter what linkage criteria,
         always returns tuples that are closest to each other
        :param linkage: Closest defined using the metric linkage
        :returns closest 2 clusters as a tuple
        """
        clusters = self.getClusters()
        otherClusters = self.getClusters()[1:]
        #find 1st closest value
        closest = -1.0

        i = 0
        for c1 in clusters:
            i+=1
            for c2 in clusters[i:]:
                distance = linkage(c1, c2)
                if closest < 0:
                    closest = distance
                    closestClusters = c1, c2
                elif distance < closest and c1 != c2:
                    closest = distance
                    closestClusters = c1, c2

        return closestClusters


    def mergeOne(self, linkage):
        """ Merges the two most similar clusters in self
        Similar - defined using the metric linkage
        :param linkage
        :returns tuple of the clusters that were merged
        """
        if len(self.getClusters()) >= 2:
            c1, c2 = self.findClosest(linkage)
            self.mergeClusters(c1, c2)
            return c1, c2

    def numClusters(self):
        return len(self.members)

    def toStr(self):
        cNames = []
        for c in self.members:
            cNames.append(c.getNames())
        cNames.sort()
        result = ''
        for i in range(len(cNames)):
            names = ''
            for n in cNames[i]:
                names += n + ', '
            names = names[:-2]
            result += '  C' + str(i) + ':' + names + '\n'
        return result

#City climate example
class City(Point):
    pass

def readCityData(fName, scale = False):
    """Assumes scale is a Boolean.  If True, features are scaled"""
    dataFile = open(fName, 'r')
    numFeatures = 0
    #Process lines at top of file
    for line in dataFile: #Find number of features
        if line[0:4] == '#end': #indicates end of features
            break
        numFeatures += 1
    numFeatures -= 1
    featureVals = []

    #Produce featureVals, cityNames
    featureVals, cityNames = [], []
    for i in range(numFeatures):
        featureVals.append([])
        
    #Continue processing lines in file, starting after comments
    for line in dataFile:
        dataLine = string.split(line[:-1], ',') #remove newline; then split
        cityNames.append(dataLine[0])
        for i in range(numFeatures):
            featureVals[i].append(float(dataLine[i+1]))
            
    #Use featureVals to build list containing the feature vectors
    #For each city scale features, if needed
    # scaling
    if scale:
        for i in range(numFeatures):
            featureVals[i] = scaleFeatures(featureVals[i])
    featureVectorList = []
    for city in range(len(cityNames)):
        featureVector = []
        for feature in range(numFeatures):
            featureVector.append(featureVals[feature][city])
        featureVectorList.append(featureVector)
    return cityNames, featureVectorList

def buildCityPoints(fName, scaling):
    cityNames, featureList = readCityData(fName, scaling)
    points = []
    for i in range(len(cityNames)):
        point = City(cityNames[i], pylab.array(featureList[i]))
        points.append(point)
    return points


#Use hierarchical clustering for cities
def hCluster(points, linkage, numClusters, printHistory):
    cS = ClusterSet(City)
    for p in points:
        cS.add(Cluster([p], City))
    history = []
    while cS.numClusters() > numClusters:
        merged = cS.mergeOne(linkage)
        history.append(merged)
    if printHistory:
        print ''
        for i in range(len(history)):
            names1 = []
            for p in history[i][0].members():
                names1.append(p.getName())
            names2 = []
            for p in history[i][1].members():
                names2.append(p.getName())
            print 'Step', i, 'Merged', names1, 'with', names2
            print ''
    print 'Final set of clusters:'
    print cS.toStr()
    return cS

def test1():
    points = buildCityPoints('cityTemps.txt', False) # without scaling
    #hCluster(points, Cluster.singleLinkageDist, 10, False)
    #points = buildCityPoints('cityTemps.txt', True)
    # hCluster(points, Cluster.maxLinkageDist, 10, False)
    # hCluster(points, Cluster.averageLinkageDist, 10, False)
    # hCluster(points, Cluster.singleLinkageDist, 10, False)
    hCluster(points, Cluster.singleLinkageDist, 5, False)

    points = buildCityPoints('cityTemps.txt', True) # with scaling
    hCluster(points, Cluster.singleLinkageDist, 5, False)

def test2():
    points = buildCityPoints('test.txt', False)
    hCluster(points, Cluster.singleLinkageDist, 3, True)
    hCluster(points, Cluster.maxLinkageDist, 3, True)
    hCluster(points, Cluster.averageLinkageDist, 3, True)



#test1() # takes cityTemps as the points (complex test)
#test2.txt() # a simple test
''' Test 2 Expected Output:
Clusters of 3, no scaling, single, max & average (respectively)
Final set of clusters:
  C0:a
  C1:b, c, d, e, g
  C2:f

Final set of clusters:
  C0:a, b, d
  C1:c, e, g
  C2:f

Final set of clusters:
  C0:a, f
  C1:b, c, d, e
  C2:g

  Results may vary: (in this case last one)
  depends on which point gets chosen in case of a tie

My Final set of clusters (last one):
Final set of clusters:
  C0:a, f
  C1:b, d
  C2:c, e, g
    c & e added to C2 cluster in average linkage case
'''



# 4 clusters used
def test3():
    points = buildCityPoints('test2.txt', False)
    hCluster(points, Cluster.singleLinkageDist, 3, False)
    hCluster(points, Cluster.maxLinkageDist, 3, False)
    hCluster(points, Cluster.averageLinkageDist, 3, False)
    hCluster(points, Cluster.mysteryLinkageDist, 3, False)

test3() # test from final exam (also uses mysteryLinkage

''' Results for test3():
Clusters = 4; No scaling
Single, Max, Average, Mystery
Final set of clusters: SINGLE
  C0:a
  C1:b, c, d
  C2:e, g
  C3:f

Final set of clusters: MAX
  C0:a
  C1:b, c, d
  C2:e, g
  C3:f

Final set of clusters: AVERAGE
  C0:a
  C1:b, c, d
  C2:e, g
  C3:f

Final set of clusters: MYSTERY
  C0:a
  C1:b, c, d
  C2:e, g
  C3:f

Cluster = 3; No Scaling: (all clusters the same)
  C0:a
  C1:b, c, d, e, g
  C2:f

'''
