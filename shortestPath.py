import networkx as nx
import matplotlib.pyplot as plt

import sys
sys.path.append("./project-sp21-skeleton")
from parse import *


def main(inputFile):
    G = read_input_file("inputs/" + inputFile)
    shortestPath(G)

def shortestPath(G, target):
    source = 0
    shortest_path = nx.algorithms.shortest_paths.weighted.dijkstra_path(G, source, target)
    shortest_path_length = nx.classes.function.path_weight(G, shortest_path, weight="weight")

    #print("The shortest path is: " + str(shortest_path))
    #print("The shortest path has length: " + str(shortest_path_length))
    return shortest_path, shortest_path_length

if __name__ == "__main__":
    main(sys.argv[1])