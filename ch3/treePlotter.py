import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_agrs = dict(arrowstyle="<-")

def plotNode(nodeTxt, centerPt, parentPt, nodeType):
	createPlot.ax.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction',
							xytext=centerPt, textcoords='axes fraction',
							va='center', ha='center', bbox=nodeType,
							arrowprops=arrow_agrs)

def createPlot():
	fig = plt.figure(1, facecolor='white')
	fig.clf()
	createPlot.ax = plt.subplot(111, frameon=False)
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

