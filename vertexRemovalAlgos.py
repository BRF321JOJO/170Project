import sys
sys.path.append("./project-sp21-skeleton")
from parse import *
from utils import calculate_score

import networkx as nx
from shortestPathFile import shortestPath
import random


"""Removes random vertex from the SP repeatedly, but weighted by heuristic. 
   Does not disconnect graph. """
def VERTEX_SPrandom(G, vertexLimit, target, heuristic):
    to_remove = []
    for i in range(vertexLimit):

        # 1. Calculate nodes on SP for current graph that do not disconnect graph
        sp = shortestPath(G, target)
        sp_nodes = sp[1:len(sp)-1]
        articulation_list = list(nx.articulation_points(G))
        sp_nodes = [node for node in sp_nodes if node not in articulation_list]

        # 2. If no nodes can be removed along SP without disconnecting graph, break loop.
        if not sp_nodes:
            break

        # 3. Sort nodes by heuristic. Remove first one.
        heuristic(G, sp_nodes)

        first_node = sp_nodes[0]
        G.remove_node(first_node)
        to_remove.append(first_node)

    return to_remove




#### Heuristics: Remove random nodes on SP ####

def VERTEX_SPtrueRandom(G, sp_nodes):
    random.shuffle(sp_nodes)

# Consider adding randomness to this degree heuristic
def VERTEX_HighestDegree(G, sp_nodes):
    sp_nodes.sort(reverse=True, key=lambda v: G.degree[v])  # Sort vertices by decreasing degree

    if len(sp_nodes) > 1:
        spice = sp_nodes[1:]
        random.shuffle(spice)
        test = random.uniform(0, 1)
        if test > 0.85:
            sp_nodes[0] = spice[0]



#### Completely random algorithm ####

""" Picks a random set of vertexLimit nodes to remove. Connot disconenct graph. Tries 100 times."""
def VERTEX_TrueRandom(G, vertexLimit, target):
    vertices = list(G.nodes())
    vertices.remove(0)
    vertices.remove(target)
    vertexLimit = min(vertexLimit, G.number_of_nodes())
    tries = 100
    while tries:
        to_remove = random.sample(vertices, k=vertexLimit)
        H = G.copy()
        H.remove_nodes_from(to_remove)
        if nx.is_connected(H):
            return to_remove
        else:
            tries -= 1
    return []
