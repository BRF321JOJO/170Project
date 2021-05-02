import sys
sys.path.append("./project-sp21-skeleton")
from parse import read_input_file
from utils import calculate_score

import networkx as nx
from vertexRemovalAlgos import *
from edgeRemovalAlgos import *


def genMaxShortestPath(H, vertexLimit, edgeLimit):
    target = H.number_of_nodes() - 1
    solutions = []

    # Solution 1: Vertex true random -> Edge repeated brute force for k=3
    # G = H.copy()
    # v3 = VERTEX_TrueRandom(G, vertexLimit, target)
    # G.remove_nodes_from(v3)
    #
    # e3 = []
    # while edgeLimit > 0:
    #    new_removed = EDGE_SP_bruteforce(G, 3, target)
    #    e3.extend(new_removed)
    #    G.remove_edges_from(new_removed)
    #    edgeLimit -= 3
    #
    # solutions.append((v3, e3))

    # Solution 2: Vertex true random -> Edge true random
    # G = H.copy()
    # v4 = VERTEX_TrueRandom(G, vertexLimit, target)
    # G.remove_nodes_from(v4)
    # e4 = EDGE_TrueRandom(G, edgeLimit)
    # solutions.append((v4, e4))

    # Solution 3: Solution 2 reversed
    # G = H.copy()
    # e4 = EDGE_TrueRandom(G, edgeLimit)
    # G.remove_edges_from(e4)
    # v4 = VERTEX_TrueRandom(G, vertexLimit, target)
    # solutions.append((v4, e4))

    # Solution 4: Vertex true random -> Edge random along SP
    # G = H.copy()
    # v7 = VERTEX_TrueRandom(G, vertexLimit, target)
    # G.remove_nodes_from(v7)
    # e7 = EDGE_SPrandom(G, edgeLimit, target, EDGE_SPtrueRandom)
    # solutions.append((v7, e7))

    # Solution 5: Solution 4 but reversed
    # G = H.copy()
    # e7 = EDGE_SPrandom(G, edgeLimit, target, EDGE_SPtrueRandom)
    # G.remove_edges_from(e7)
    # v7 = VERTEX_TrueRandom(G, vertexLimit, target)
    # solutions.append((v7, e7))

    # Solution 6: Vertex random along SP -> Edge random along SP
    # G = H.copy()
    # v5 = VERTEX_SPrandom(G, vertexLimit, target, VERTEX_SPtrueRandom)
    # G.remove_nodes_from(v5)
    # e5 = EDGE_SPrandom(G, edgeLimit, target, EDGE_SPtrueRandom)
    # solutions.append((v5, e5))

    # Solution 7: Solution 6 reversed
    # G = H.copy()
    # e6 = EDGE_SPrandom(G, edgeLimit, target, EDGE_SPtrueRandom)
    # G.remove_edges_from(e6)
    # v6 = VERTEX_SPrandom(G, vertexLimit, target, VERTEX_SPtrueRandom)
    # solutions.append((v6, e6))

    # Solution 8: Vertex SP random -> Edge SP random, weighted by smallest
    # G = H.copy()
    # v8 = VERTEX_SPrandom(G, vertexLimit, target, VERTEX_SPtrueRandom)
    # G.remove_nodes_from(v8)
    # e8 = EDGE_SPrandom(G, edgeLimit, target, EDGE_shortest)
    # solutions.append((v8, e8))

    # Solution 9: Vertex SP random -> Edge SP random, weighted by largest
    # G = H.copy()
    # v9 = VERTEX_SPrandom(G, vertexLimit, target, VERTEX_SPtrueRandom)
    # G.remove_nodes_from(v9)
    # e9 = EDGE_SPrandom(G, edgeLimit, target, EDGE_shortestReversed)
    # solutions.append((v9, e9))

    # Solution 10: Vertex SP random -> Edge SP random, weighted by expovariate
    # G = H.copy()
    # v10 = VERTEX_SPrandom(G, vertexLimit, target, VERTEX_SPtrueRandom)
    # G.remove_nodes_from(v10)
    # e10 = EDGE_SPrandom(G, edgeLimit, target, EDGE_Expovariate)
    # solutions.append((v10, e10))

    # Solution 11: Vertex SP random -> Edge SP random, weighted by minimizing the creation of bridges
    # G = H.copy()
    # v11 = VERTEX_SPrandom(G, vertexLimit, target, VERTEX_SPtrueRandom)
    # G.remove_nodes_from(v11)
    # e11 = EDGE_SPrandom(G, edgeLimit, target, EDGE_avoidMakingBridges)
    # solutions.append((v11, e11))

    # Solution 12: Solution 11 but reversed
    G = H.copy()
    e12 = EDGE_SPrandom(G, edgeLimit, target, EDGE_avoidMakingBridges)
    G.remove_edges_from(e12)
    v12 = VERTEX_SPrandom(G, vertexLimit, target, VERTEX_SPtrueRandom)
    solutions.append((v12, e12))

    # Solution 21: Vertex true random -> Edge SP random, weighted by minimizing the creation of bridges
    # G = H.copy()
    # v11 = VERTEX_TrueRandom(G, vertexLimit, target)
    # G.remove_nodes_from(v11)
    # e11 = EDGE_SPrandom(G, edgeLimit, target, EDGE_avoidMakingBridges)
    # solutions.append((v11, e11))

    # Solution 22: Solution 21 reversed
    # G = H.copy()
    # e11 = EDGE_SPrandom(G, edgeLimit, target, EDGE_avoidMakingBridges)
    # G.remove_edges_from(e11)
    # v11 = VERTEX_TrueRandom(G, vertexLimit, target)
    # solutions.append((v11, e11))


    # Solution 13: Edges along SP weighted by most vital


    return max(solutions, key=lambda x: calculate_score(H, x[0], x[1]))


def main(inputFile, nodeLimit, edgeLimit):
    G = read_input_file("project-sp21-skeleton/inputs/" + inputFile)
    return genMaxShortestPath(G, nodeLimit, edgeLimit)

if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))



#### Old solutions ####

# Solution 1: Edge shortest on SP -> Vertex highest degree
# G = H.copy()
# e1 = EDGEremoveGreedyShortest(G, edgeLimit, target)
# v1 = VERTEXremoveGreedyHighestDegree(G, vertexLimit, target)
# solutions.append((v1, e1))

# Solution 2: Vertex highest degree -> Edge shortest on SP
# G = H.copy()
# v2 = VERTEXremoveGreedyHighestDegree(G, vertexLimit, target)
# e2 = EDGEremoveGreedyShortest(G, edgeLimit, target)
# solutions.append((v2, e2))
