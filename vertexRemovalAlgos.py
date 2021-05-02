import sys
sys.path.append("./project-sp21-skeleton")
from parse import *
from utils import calculate_score

import networkx as nx
from shortestPathFile import shortestPath
import random


def VERTEXremoveGreedyHighestDegree(G, vertexLimit, target):
    removed_nodes = []
    for i in range(vertexLimit):  # Remove vertexLimit vertices
        sp = shortestPath(G, target)  # Calculate new shortest path in G
        sp = sp[1:len(sp)-1]   # Don't consider s and t for removal
        sp.sort(reverse=True, key=lambda v: G.degree[v])  # Sort vertices by decreasing degree

        for vertex in sp:
            if vertex not in nx.articulation_points(G):  # If removing this vertex would not disconnect graph
                G.remove_node(vertex)
                removed_nodes.append(vertex)
                break

    return removed_nodes



def VERTEXremoveSPrandom(G, vertexLimit, target):
    removed_vertices = []
    for i in range(vertexLimit):  # Remove vertexLimit nodes
        sp = shortestPath(G, target)  # Calculate new shortest path in G
        sp = sp[1:len(sp)-1]
        random.shuffle(sp)

        update = False
        for vertex in sp:
            if vertex not in nx.articulation_points(G):  # Don't remove node that disconnects graph
                update = True
                G.remove_node(vertex)
                removed_vertices.append(vertex)
                break

        if not update:  # Break loop when shortest path cannot increase without disconnecting graph
            break

    return removed_vertices


def VERTEXremoveRandomized(G, vertexLimit, target):
    vertices = list(G.nodes())
    vertices.remove(0)
    vertices.remove(target)
    vertexLimit = min(vertexLimit, len(vertices))

    while vertexLimit > 0:
        to_remove = random.sample(vertices, k=vertexLimit)
        H = G.copy()
        H.remove_nodes_from(to_remove)

        if not nx.is_connected(H):
            vertexLimit -= 1
        else:
            return to_remove

    print("OUTPUT FAILED ENTIRELY, vertices")
    return []
