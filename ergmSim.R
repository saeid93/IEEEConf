"This script is in charge of making 
  doing the ergm simulations"

rm(list=ls())
setwd("/home/saeid/R projects/IEEEconf")
library(statnet)
load("CA-HepTh(9877)idfixed.Rdata")

numOfSim = 100 # number of desired simulations
# netModel <- ergm(net ~ edges + density + triangles + isolates + gwdegree(0.25) + gwdsp + gwesp + gwnsp)
start.time <- Sys.time()
netModel <- ergm(net ~ edges + density + triangles + isolates + gwdegree(0.25))
end.time <- Sys.time()
time.taken <- end.time - start.time

start.time <- Sys.time()
simulatedNet <- simulate(netModel, nsim=1)
end.time <- Sys.time()
time.taken <- end.time - start.time
