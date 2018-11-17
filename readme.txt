building the graph from the data operations:
1. The python script fixIds.py is run in order to fix id numerics. (some datasets ids are does not start from 1 to #of edges)
2. If the dataset is not in a undirected form then we have to make it. (not yet implemented)
3. The readInput.R file is used to make the graph from the data in R.(the assimngment part is not efficient)
4. The script buildModel.R, build the model based on the graph. It uses the R data the was mede from the dataset.
5. The script simulation.R is used to build 100 (or more) simulated graphs from the data.
6. The aveGraphs.py is used to average over the simulated graphs and build the diffusion graph.
