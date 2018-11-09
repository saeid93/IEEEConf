import numpy as np
import os
import networkx as nx


def save_sparse_matrix(m,filename):
    thefile = open(filename, 'w')
    nonZeros = np.array(m.nonzero())
    for entry in range(nonZeros.shape[1]):
        thefile.write("%s,%s,%s\n" % (nonZeros[0, entry], nonZeros[1, entry], m[nonZeros[0, entry], nonZeros[1, entry]]))

# # number of graph nodes
numOfNodes = 9877

# list the files in the simulated graphs directory
files  = os.listdir('simNets/')
adjLists = []

# read the grpahs adjacency lists
for file in files:
    adjLists = adjLists + [np.genfromtxt ('simNets/'+file, delimiter=",")]



# build the graph
diffGraph = nx.empty_graph(numOfNodes)
counter = 1
numOfFiles = 1/100
diffGraph = nx.empty_graph(numOfNodes)
for adjList in adjLists:
    numOfele = np.shape(adjList)[0]
    for i in range(0, numOfele):
        rowIndex = int(adjList[i,0]) - 1
        colIndex = int(adjList[i,1]) - 1
        if diffGraph.has_edge(rowIndex,colIndex):
            diffGraph[rowIndex][colIndex]['weight'] = diffGraph[rowIndex][colIndex]['weight'] + numOfFiles
        else:
            diffGraph.add_edge(rowIndex,colIndex,weight=numOfFiles)
    print("file "+str(counter)+" completed")
    counter = counter + 1

diffGraph = nx.to_scipy_sparse_matrix(diffGraph)
# print(diffGraph.todense())
# write matrix to file
save_sparse_matrix(diffGraph,'diffMatrix.csv')
