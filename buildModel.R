"This script is in charge of building the 
  ergm model"

rm(list=ls())
curDir = "/home/saeid/R projects/IEEEconf"
setwd(curDir)
library(statnet)
adjMatFile = "CA-HepTh(9877)idfixed.Rdata" 
load(adjMatFile)


# build the model from the network
start.time <- Sys.time()
netModel <- ergm(net ~ edges + density + triangles + isolates + gwdegree(0.25) + gwdsp + gwesp + gwnsp)
end.time <- Sys.time()
save(netModel, file = "netModelRdata.Rdata")

