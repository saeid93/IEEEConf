"This script is in charge of making 
  doing the ergm simulations"

# rm(list=ls())
# curDir = "/home/saeid/R projects/IEEEconf"
# setwd(curDir)
# modelFile = "netModelRdata.Rdata"
# netModel = load(modelFile)

numOfSim = 100 # number of desired simulations

for (i in 1:numOfSim){
  simulatedNet <- simulate(netModel, nsim=1)
  simulatedNet <- as.matrix(simulatedNet, matrix.type = 'edgelist')
  write.table( simulatedNet, paste(i,"simNet.csv",sep = ""), sep=",",  col.names=FALSE, row.names = FALSE)
  print(paste("network number",i,"has successfuly been created"))
  rm(simulatedNet)
}

