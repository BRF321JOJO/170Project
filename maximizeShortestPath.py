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

    # Solution 1
    # G = H.copy()
    # e1 = EDGEremoveGreedyShortest(G, edgeLimit, target)
    # v1 = VERTEXremoveGreedyHighestDegree(G, vertexLimit, target)
    # solutions.append((v1, e1))

    # Solution 2
    # G = H.copy()
    # v2 = VERTEXremoveGreedyHighestDegree(G, vertexLimit, target)
    # e2 = EDGEremoveGreedyShortest(G, edgeLimit, target)
    # solutions.append((v2, e2))

    # Solution 3
    # Try repeated k=5 brute forces
    # G = H.copy()
    # v3 = VERTEXremoveRandomized(G, vertexLimit, target)
    # G.remove_nodes_from(v3)
    # e3 = []
    # while edgeLimit > 0:
    #    new_removed = EDGEremoveBruteForce(G, 3, target)
    #    e3.extend(new_removed)
    #    G.remove_edges_from(new_removed)
    #    edgeLimit -= 3
    # solutions.append((v3, e3))

    # Solution 4: Randomized
    # G = H.copy()
    # v4 = VERTEXremoveRandomized(G, vertexLimit, target)
    # G.remove_nodes_from(v4)
    # e4 = EDGEremoveRandomized(G, edgeLimit)
    # solutions.append((v4, e4))

    # Solution 5: Random over SP
    # G = H.copy()
    # v5 = VERTEXremoveSPrandom(G, vertexLimit, target)
    # G.remove_nodes_from(v5)
    # e5 = EDGEremoveSPrandom(G, edgeLimit, target)
    # solutions.append((v5, e5))

    # Solution 6: Random over SP reversed
    G = H.copy()
    e6 = EDGEremoveSPrandom(G, edgeLimit, target)
    G.remove_edges_from(e6)
    v6 = VERTEXremoveSPrandom(G, vertexLimit, target)
    solutions.append((v6, e6))

    # Solution 7: Random vertex, edges over SP
    # G = H.copy()
    # v5 = VERTEXremoveRandomized(G, vertexLimit, target)
    # G.remove_nodes_from(v5)
    # e5 = EDGEremoveSPrandom(G, edgeLimit, target)
    # solutions.append((v5, e5))

    # Solution 8: Random along SP with weight to lighter edges
    # G = H.copy()
    # v8 = VERTEXremoveSPrandom(G, vertexLimit, target)
    # G.remove_nodes_from(v8)
    # e8 = EDGEremoveSPrandomWEIGHTED(G, edgeLimit, target)
    # solutions.append((v8, e8))

    # Solution 9: Random along SP with reversed weights to lighter edges
    # G = H.copy()
    # v9 = VERTEXremoveSPrandom(G, vertexLimit, target)
    # G.remove_nodes_from(v9)
    # e9 = EDGEremoveSPrandomWEIGHTEDreversed(G, edgeLimit, target)
    # solutions.append((v9, e9))

    # Solution 10: SP randomized, weighted to lighter edges with poisson distribution
    # G = H.copy()
    # v10 = VERTEXremoveSPrandom(G, vertexLimit, target)
    # G.remove_nodes_from(v10)
    # e10 = EDGEremoveSPrandomWEIGHTEDexpovariate(G, edgeLimit, target)
    # solutions.append((v10, e10))

    # Solution 11: Edges along SP weighted by vitality


    #Maximize over the solutions
    return max(solutions, key=lambda x: calculate_score(H, x[0], x[1]))


def main(inputFile, nodeLimit, edgeLimit):
    G = read_input_file("project-sp21-skeleton/inputs/" + inputFile)
    return genMaxShortestPath(G, nodeLimit, edgeLimit)

if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
