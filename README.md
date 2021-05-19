# CS170 Spring 2021 Project:
This is our attempt at a solver for a version of the network interdiction problem.

- Given a graph G, remove a limited number of edges and vertices to maximize the shortest path from s to t without disconnecting the graph.
***

### PLACEMENT:
Our team got 8th place out of 239 teams in CS170 (Spring 2021).
![CS170_Project_Leaderboard](https://user-images.githubusercontent.com/26397543/118769555-26489300-b835-11eb-9373-1525e91e4bc4.png)
*Excuse our silly name :)
***

## Running The Code
### DEPENDENCIES:

Please install networkx with pip3:
```bash
pip3 install networkx
```
***
### RUN INSTRUCTIONS:

First, change directory into the project-sp21-skeleton folder:
```bash
cd 170Project/project-sp21-skeleton
```

**Generate a batch of outputs**:
```bash
python3 batchSolver.py 3
```

**The argument to batchSolver.py specifies the number of iterations to run.**

***
### CHANGE HEURISTIC

Batches are generated with a specified heuristic.

The heuristic can be changed in maximizeShortestPath.py (in the 170Project directory).

Comment out the current heuristic and uncomment a different one.


A heuristic will be of the form:
```python
# Description of the heuristic
G = H.copy()
x = #Function call for removal of edges/nodes
G.remove_(x_type)_from(x)
y = #Function call for removal of edges/nodes
solutions.append((x, y))
```

For example:
```python
# Solution 11: Vertex SP random -> Edge SP random, weighted by minimizing the creation of bridges
G = H.copy()
v11 = VERTEX_SPrandom(G, vertexLimit, target, VERTEX_SPtrueRandom)
G.remove_nodes_from(v11)
e11 = EDGE_SPrandom(G, edgeLimit, target, EDGE_avoidMakingBridges)
solutions.append((v11, e11))
```
