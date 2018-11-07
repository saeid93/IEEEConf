rm(list=ls())
setwd("/home/saeid/R projects/IEEEconf")
library(statnet)

# read the adjacency list from the file
filename <- "CA-HepTh(9877)idfixed"
adjList <- read.csv(paste(filename,".csv",sep = ""),header=FALSE,stringsAsFactors=FALSE)
adjList <- as.matrix(adjList)
# initialize the network
numOfNodes <- 9877
net <- network.initialize(numOfNodes, directed = TRUE)

numOfEdges <- nrow(adjList)
for (i in 1:numOfEdges){
   print(i)
   net[adjList[i,1],adjList[i,2]] <- 1
 }
 
 save(net, file = paste(filename,".Rdata",sep = ""))

# set network nonzero edges
net[adjList] <- 1

