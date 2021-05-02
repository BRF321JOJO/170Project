import sys
sys.path.append("./project-sp21-skeleton")
from parse import *
from utils import calculate_score

import networkx as nx
from shortestPathFile import shortestPath
import random


def EDGEremoveRandomized(G, edgeLimit):
    edgeLimit = min(edgeLimit, G.number_of_edges())

    while edgeLimit > 0:
        to_remove = random.sample(G.edges(), k=edgeLimit)
        H = G.copy()
        H.remove_edges_from(to_remove)

        if not nx.is_connected(H):
            edgeLimit -= 1
        else:
            return to_remove

    print("OUTPUT FAILED ENTIRELY, edges")
    return []

def EDGEremoveGreedyShortest(G, edgeLimit, target):
    removed_edges = []
    for i in range(edgeLimit):  # Remove edgeLimit edges
        sp = shortestPath(G, target)  # Calculate new shortest path in G
        sp_edges = [(sp[i], sp[i+1]) for i in range(len(sp) - 1)]  # Convert shortest path to list of edges
        sp_edges.sort(key=lambda edge: G[edge[0]][edge[1]]['weight'])  # Sort edges by increasing weight

        update = False
        for edge in sp_edges:
            edgeReverse = (edge[1], edge[0])
            bridgeList = list(nx.bridges(G))
            if (edge not in bridgeList) and (edgeReverse not in bridgeList):  # Don't remove edge that disconnects graph
                update = True
                G.remove_edge(edge[0], edge[1])
                removed_edges.append(edge)
                break

        if not update:  # Break loop when shortest path cannot increase without disconnecting graph
            break

    return removed_edges


def EDGEremoveSPrandomWEIGHTED(G, edgeLimit, target):
    removed_edges = []
    for i in range(edgeLimit):  # Remove edgeLimit edges
        sp = shortestPath(G, target)  # Calculate new shortest path in G
        sp_edges = [(sp[i], sp[i + 1]) for i in range(len(sp) - 1)]  # Convert shortest path to list of edges
        random.shuffle(sp_edges)

        if len(sp_edges) > 1:
            weight = sp_edges[0:2]
            weight.sort(key=lambda edge: G[edge[0]][edge[1]]['weight'])
            sp_edges[0:2] = weight[0:2]

        update = False
        for edge in sp_edges:
            edgeReverse = (edge[1], edge[0])
            bridgeList = list(nx.bridges(G))
            if (edge not in bridgeList) and (edgeReverse not in bridgeList):  # Don't remove edge that disconnects graph
                update = True
                G.remove_edge(edge[0], edge[1])
                removed_edges.append(edge)
                break

        if not update:  # Break loop when shortest path cannot increase without disconnecting graph
            break

    return removed_edges


def EDGEremoveSPrandomWEIGHTEDreversed(G, edgeLimit, target):
    removed_edges = []
    for i in range(edgeLimit):  # Remove edgeLimit edges
        sp = shortestPath(G, target)  # Calculate new shortest path in G
        sp_edges = [(sp[i], sp[i + 1]) for i in range(len(sp) - 1)]  # Convert shortest path to list of edges
        random.shuffle(sp_edges)

        if len(sp_edges) > 4:
            weight = sp_edges[0:5]
            weight.sort(key=lambda edge: G[edge[0]][edge[1]]['weight'], reverse=True)
            sp_edges[0:5] = weight[0:5]

        update = False
        for edge in sp_edges:
            edgeReverse = (edge[1], edge[0])
            bridgeList = list(nx.bridges(G))
            if (edge not in bridgeList) and (edgeReverse not in bridgeList):  # Don't remove edge that disconnects graph
                update = True
                G.remove_edge(edge[0], edge[1])
                removed_edges.append(edge)
                break

        if not update:  # Break loop when shortest path cannot increase without disconnecting graph
            break

    return removed_edges

def EDGEremoveSPrandomWEIGHTEDexpovariate(G, edgeLimit, target):
    removed_edges = []
    for i in range(edgeLimit):  # Remove edgeLimit edges
        sp = shortestPath(G, target)  # Calculate new shortest path in G
        sp_edges = [(sp[i], sp[i + 1]) for i in range(len(sp) - 1)]  # Convert shortest path to list of edges
        random.shuffle(sp_edges)

        sp_edges.sort(key=lambda x: random.expovariate(0.5*G[x[0]][x[1]]['weight']))

        update = False
        for edge in sp_edges:
            edgeReverse = (edge[1], edge[0])
            bridgeList = list(nx.bridges(G))
            if (edge not in bridgeList) and (edgeReverse not in bridgeList):  # Don't remove edge that disconnects graph
                update = True
                G.remove_edge(edge[0], edge[1])
                removed_edges.append(edge)
                break

        if not update:  # Break loop when shortest path cannot increase without disconnecting graph
            break

    return removed_edges

def EDGEremoveSPrandom(G, edgeLimit, target):
    removed_edges = []
    for i in range(edgeLimit):  # Remove edgeLimit edges
        sp = shortestPath(G, target)  # Calculate new shortest path in G
        sp_edges = [(sp[i], sp[i + 1]) for i in range(len(sp) - 1)]  # Convert shortest path to list of edges
        random.shuffle(sp_edges)

        update = False
        for edge in sp_edges:
            edgeReverse = (edge[1], edge[0])
            bridgeList = list(nx.bridges(G))
            if (edge not in bridgeList) and (edgeReverse not in bridgeList):  # Don't remove edge that disconnects graph
                update = True
                G.remove_edge(edge[0], edge[1])
                removed_edges.append(edge)
                break

        if not update:  # Break loop when shortest path cannot increase without disconnecting graph
            break

    return removed_edges

def EDGEremoveBruteForce(G, edgeLimit, target):
    if edgeLimit == 0:
        return []

    # Function returns a list of edges to remove that maximizes the shortest path
    sp = shortestPath(G, target)
    sp_edges = [(sp[i], sp[i + 1]) for i in range(len(sp) - 1)]

    edgeDict = {}
    for edge in sp_edges:
        edgeReverse = (edge[1], edge[0])
        bridgeList = list(nx.bridges(G))

        if (edge not in bridgeList) and (edgeReverse not in bridgeList):
            H = G.copy()
            H.remove_edge(edge[0], edge[1])

            # Recursive call returns list of edges to remove that maximizes the shortest path from graph with "edge" removed
            optimal_removed = EDGEremoveBruteForce(H, edgeLimit - 1, target)
            all_removed = [edge] + list(optimal_removed)

            H.add_edge(edge[0], edge[1])
            H.remove_edges_from(all_removed)
            edgeDict[tuple(all_removed)] = shortestPath(H, target)

    if not edgeDict:
        return []
    return list(max(edgeDict, key=lambda x: edgeDict[x]))