from numpy import *
import operator

def createDataSet():
	group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
	labels = ['A', 'A', 'B', 'B']
	return group, labels


def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances ** 0.5
	sortedDistIndices = distances.argsort()

	classCount = {}
	for i in range(k):
		voteILabel = labels[sortedDistIndices[i]]
		classCount[voteILabel] = classCount.get(voteILabel, 0) + 1

	print classCount


	sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse = True)

	return sortedClassCount, classCount


def file2matrix(filename):
	fr = open(filename)
	numberOfLines = len(fr.readlines())
	fr.close()

	returnMat = zeros((numberOfLines, 3))
	classLabelVector = []

	fr = open(filename)
	index = 0

	for line in fr.readlines():
		line = line.strip()
		listFromLine = line.split('\t')
		returnMat[index, : ] = listFromLine[0:3]
		classLabelVector.append(listFromLine[-1])
		index += 1

	return returnMat, classLabelVector

def autoNorm(dataSet):
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - tile(minVals, (m, 1))
	normDataSet = normDataSet / tile(ranges, (m, 1))

	return normDataSet, ranges, minVals
