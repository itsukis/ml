from os import listdir
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

	sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse = True)

	return int(sortedClassCount[0][0])


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


def datingClassTest():
	hoRatio = 0.10
	datingDataMat, datingLabels = file2matrix("datingTestSet2.txt")
	normMat, ranges, minVals = autoNorm(datingDataMat)
	
	m = normMat.shape[0]
	numTestVecs = int(m * hoRatio)
	errorCount = 0.0
	for i in range(numTestVecs):
		classifierResult = classify0(normMat[i,:], normMat[numTestVecs:m,:], datingLabels[numTestVecs:m], 3)
		#print classifierResult, datingLabels[i]
		print "the classifier came back with %d, the real answer is %d" % (classifierResult, int(datingLabels[i]))

		if (classifierResult != int(datingLabels[i])):
			errorCount += 1.0
	
	print "The total error rate is: %f" % (errorCount/float(numTestVecs))

def img2vector(filename):
	returnVect = zeros((1, 1024))
	fr = open(filename)
	for i in range(32):
		lineStr = fr.readline()
		for j in range(32):
			returnVect[0, i*32 + j] = int(lineStr[j])
	return returnVect

def handwritingClassTest():
	
	##
	## Training Data Set
	##
	hwLables = []
	trainingFileList = listdir('digits/trainingDigits')
	m = len(trainingFileList)
	trainingMat = zeros((m, 1024))

	for i in range(m):
		fileNameStr = trainingFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		hwLables.append(classNumStr)
		trainingMat[i, :] = img2vector('digits/trainingDigits/%s' % (fileNameStr))

	##
	## Test Data Set
	##
	testFileList = listdir('digits/testDigits')
	mTest = len(testFileList)
	errorCount = 0.0
	
	for i in range(mTest):
		fileNameStr = testFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		vectorUnderTest = img2vector('digits/testDigits/%s' % (fileNameStr))
		classifierResult = classify0(vectorUnderTest, trainingMat, hwLables, 3)

		print "the classifier came back with %d, the real answer is %d" % (classifierResult, classNumStr)

		if (classifierResult != classNumStr): errorCount += 1.0

	print "the total number of errors is %d" % errorCount
	print "the total error rate is %f" % (errorCount/float(mTest))
