from math import log
import operator

def createDataSet():
	dataSet = [[1, 1, 'yes'],
			   [1, 1, 'yes'],
			   [1, 0, 'no'],
			   [0, 1, 'no'],
			   [0, 1, 'no']]
	labels = ['no surfacing', 'flippers']

	return dataSet, labels

def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts = {}

	for featVect in dataSet:
		currentLabel = featVect[-1]
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] += 1

	shannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key])/numEntries
		shannonEnt -= prob * log(prob, 2)

	return shannonEnt

def splitDataSet(dataSet, axis, value):
	retDataSet = []
	for featVect in dataSet:
		if (featVect[axis] == value) :
			reducedFeatVect = featVect[:axis]
			reducedFeatVect.extend(featVect[axis+1:])
			retDataSet.append(reducedFeatVect)
	return retDataSet

def chooseBestFeatureToSplit(dataSet):
	numFeatures = len(dataSet[0]) - 1
	baseEntropy = calcShannonEnt(dataSet)
	bestInfoGain = 0.0; bestFeature = -1

	for i in range(numFeatures):
		featList = [example[i] for example in dataSet]
		uniqueVals = set(featList)
		newEntropy = 0.0

		# Calculate the expectation of entropy of each feature 
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet, i, value)
			prob = len(subDataSet) / float(len(dataSet))
			newEntropy += prob * calcShannonEnt(subDataSet)
		
		infoGain = baseEntropy - newEntropy
		if (infoGain > bestInfoGain) :
			bestInfoGain = infoGain
			bestFeature = i

	return bestFeature

def majorityCount(classList):
	classCount = {}
	for vote in classList:
		if vote not in classCount.keys(): classCount[vote] = 0
		classCount[vote] += 1
	sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=yes)

	return sortedClassCount[0][0]

def createTree(dataSet, labels):
	classList = [example[-1] for example in dataSet]
	## there are items which are classified as the same
	if classList.count(classList[0]) == len(classList):
		return classList[0]
	## only classified one left ('yes' of 'no')
	if len(dataSet[0]) == 1:
		return majorityCount(classList)

	bestFeat = chooseBestFeatureToSplit(dataSet)
	bestFeatLabel = labels[bestFeat]
	myTree = {bestFeatLabel : {}}
	del(labels[bestFeat])

	featValues = [example[bestFeat] for example in dataSet]
	uniqueVals = set(featValues)
	for value in uniqueVals:
		subLabels = labels[:]
		myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)

	return myTree


