import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

'''
Std Dev (from lecture)
'''
def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

'''Coefficient of Variance
'''
def CV(X):
    mean = sum(X)/float(len(X))
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('NaN')

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList




def labelPlot(mean, sd):
    pylab.title('Histogram: Proportion of Vowels in Words in words.txt')
    pylab.xlabel('Proportion of Vowels')
    pylab.ylabel('Number of words')
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    #adds a text plot
    # pylab.text(1st two args, where to put args...)
    pylab.text(xmin + (xmax-xmin)*0.02, (ymax-ymin)*2,
               'Mean = ' + str(round(mean, 4))
               + '\nSD = ' + str(round(sd, 4))
               + '\nCV = ' + str(round(sd/mean, 4)))




def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    vowelprops = [] #initialize list containing proportions (vowels in word/all chars)
    vowels = 0 #initialize counter of vowels
    for word in wordList:
        vowels = 0.0 #set to 0 again NOTE: need to set this to float
        for c in word:
            if c=="a" or c=='e' or c=='i' or c=='o' or c=='u':
                vowels+=1
        vp = vowels/len(word)
        vowelprops.append(vp)


    #plot for histogram
    mean = sum(vowelprops)/float(len(vowelprops))
    sd = stdDev(vowelprops)
    try:
        cv = sd/mean
    except ZeroDivisionError:
        cv = float('NaN')
    print("cv = ", str(cv))

    labelPlot(mean,sd)

    pylab.hist(vowelprops, bins = numBins)
    pylab.xlim(0, 1.1) #sets the values of x-min & x-max
    pylab.ylim()
    pylab.show()
    

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
