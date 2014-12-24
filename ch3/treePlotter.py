import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_agrs = dict(arrowstyle="<-")

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
	createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction',
							xytext=centerPt, textcoords='axes fraction',
							va='center', ha='center', bbox=nodeType,
							arrowprops=arrow_agrs)

def createPlot_t():
	fig = plt.figure(1, facecolor='white')
	fig.clf()
	createPlot.ax1 = plt.subplot(111, frameon=False)
	plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
	plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
	
	createPlot.ax.annotate("test", xy=(0.5, 0.5), xycoords="axes fraction",
						xytext=(0.8, 0.8), textcoords="axes fraction",
						va='center', ha='center', bbox=dict(boxstyle="square", fc="0.8"),
						arrowprops=dict(arrowstyle="->"))
	plt.show()

def retrieveTree(i):
	listOfTree = [{'no surfacing' : {0 : 'no', 1 : {'floppers' :
											{0 : 'no', 1 : 'yes'}}}},
											{'no surfacing' : {0 : 'no', 1 : {'floppers' :
											 {0 : {'head' : {0 : 'no', 1 : 'yes'}}, 1 : 'no'}}}}
				  ]
	return listOfTree[i]

def getNumLeafs(myTree):
	numLeafs = 0
	firstStr = myTree.keys()[0]
	secondDict = myTree[firstStr]

	for key in secondDict.keys():
		if type(secondDict[key]).__name__ == 'dict':
			numLeafs += getNumLeafs(secondDict[key])
		else:
			numLeafs += 1

	return numLeafs

def getTreeDepth(myTree):
	maxDepth = 0
	firstStr = myTree.keys()[0]
	secondDict = myTree[firstStr]

	for key in secondDict.keys():
		if type(secondDict[key]).__name__ == 'dict':
			thisDepth = 1 + getTreeDepth(secondDict[key])
		else:
			thisDepth = 1
		if thisDepth > maxDepth: maxDepth = thisDepth

	return maxDepth

def plotMidText(cntrPt, parentPt, txtString):
	xMid = (parentPt[0] - cntrPt[0])/2.0 + cntrPt[0]
	yMid = (parentPt[1] - cntrPt[1])/2.0 + cntrPt[1]

	print '%s : (%f, %f)' % (txtString, xMid, yMid)
	createPlot.ax1.text(xMid, yMid, txtString)
	return

def plotTree(myTree, parentPt, nodeTxt):
	numLeafs = getNumLeafs(myTree)
	firstStr = myTree.keys()[0]

	cntrPt = (plotTree.xOff + (1.0 + float(numLeafs))/2.0/plotTree.totalW, plotTree.yOff)
	print 'cntrPt ', cntrPt, 'parentPt ', parentPt

	plotMidText(cntrPt, parentPt, nodeTxt)
	plotNode(firstStr, cntrPt, parentPt, decisionNode)

	secondDict = myTree[firstStr]
	plotTree.yOff = plotTree.yOff - (1.0/plotTree.totalD)

	for key in secondDict.keys():



def createPlot(inTree):
	fig = plt.figure(1, facecolor='white')
	fig.clf()
	axprops = dict(xticks=[], yticks=[])
	createPlot.ax1 = plt.subplot(111, frameon=False)  #, **axprops)

	plotTree.totalW = float(getNumLeafs(inTree))
	plotTree.totalD = float(getTreeDepth(inTree))

	plotTree.xOff = -0.5/plotTree.totalW
	plotTree.yOff = 1.0

	print 'Leafs %d, Depth %d' % (plotTree.totalW, plotTree.totalD)
	print plotTree.xOff, plotTree.yOff

	plotTree(inTree, (0.5, 1.0), '123')
	plt.show()