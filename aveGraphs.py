import numpy as np
import os

# # number of graph nodes
numOfNodes = 9877

# list the files in the simulated graphs directory
files  = os.listdir('simNets/')
adjLists = []

# read the grpahs adjacency lists
for file in files:
    adjLists = adjLists + [np.genfromtxt ('simNets/'+file, delimiter=",")]

# build diffusion probability adj list (not memory efficient but fast)
diffList = np.zeros((numOfNodes,numOfNodes))
counter = 0

counter = 1
for adjList in adjLists:
    numOfele = np.shape(adjList)[0]
    for i in range(0, numOfele):
        rowIndex = int(adjList[i,0]) - 1
        colIndex = int(adjList[i,1]) - 1
        diffList[rowIndex,colIndex] = diffList[rowIndex,colIndex] + 1
    print("file "+str(counter)+" completed")
    counter = counter + 1

diffList = diffList/100
np.savetxt("diffList.csv", diffList, delimiter=",")