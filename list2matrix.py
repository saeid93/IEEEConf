import numpy as np
import networkx as nx

numOfNodes = 317080
adjList = np.loadtxt("com-dblp.csv", delimiter=',')
numOfEdges = np.shape(adjList)[0]
adjMatrix = np.zeros((numOfNodes,numOfNodes))

for i in range(0,numOfEdges):
    print(i)
    adjMatrix[adjList[i,0],adjList[i,1]] = 1