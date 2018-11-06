import numpy as np

filename = "CA-HepTh(9877)"
adjList = np.loadtxt(filename + ".csv", delimiter=',')

allNodes = np.unique(adjList)
numOfNodes = np.shape(allNodes)[0]
for i in range(0,numOfNodes):
    np.place(adjList,adjList==allNodes[i],i)


np.savetxt(filename + "idfixed.csv",adjList)

