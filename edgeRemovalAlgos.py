import sys
sys.path.append("./project-sp21-skeleton")
from parse import *
from utils import calculate_score

import networkx as nx
from shortestPathFile import shortestPath
import random


"""Removes random edge from the SP repeatedly, but weighted by heuristic. 
   Does not disconnect graph. """
def EDGE_SPrandom(G, edgeLimit, target, heuristic):
    #####
    #cumulative = 0
    #####

    to_remove = []
    for i in range(edgeLimit):

        # 1. Calculate edges on SP that do not disconnect current graph.
        sp = shortestPath(G, target)
        sp_edges = [(sp[i], sp[i + 1]) for i in range(len(sp) - 1)]
        bridgeList = list(nx.bridges(G))
        sp_edges = [edge for edge in sp_edges if (edge not in bridgeList) and (edge[::-1] not in bridgeList)]

        ####
        # print("Don't remove: " + str(bridgeList))
        # print("Considered for removal: " + str(sp_edges))
        # print("Iteration: " + str(i))
        ####

        # 2. If no edges can be removed along SP without disconnecting graph, break loop. Can no longer improve.
        if not sp_edges:
            break

        ########
        # test = sp_edges.copy()
        # test.sort(key=lambda edge: G[edge[0]][edge[1]]['weight'])
        ########

        # 3. Sort edges by heuristic. Remove first one.
        heuristic(G, sp_edges)

        ############
        # if sp_edges[0] == test[0]:
        #     cumulative += 1
        # print("Average accuracy: " + str(cumulative / (i + 1)))
        ################

        first_edge = sp_edges[0]
        G.remove_edge(first_edge[0], first_edge[1])
        to_remove.append(first_edge)

    return to_remove


#### Heuristics: Remove random edges on SP ####

""" Shuffles edges. Then sorts first X inputs by smallest weight. """
def EDGE_shortest(G, sp_edges):
    X = 3
    random.shuffle(sp_edges)
    if len(sp_edges) >= X:
        weight = sp_edges[0:X]
        weight.sort(key=lambda edge: G[edge[0]][edge[1]]['weight'])
        sp_edges[0:X] = weight[0:X]

""" Shuffes edges. Then sorts first X inputs by largest weight. """
def EDGE_shortestReversed(G, sp_edges):
    X = 3
    random.shuffle(sp_edges)
    if len(sp_edges) >= X:
        weight = sp_edges[0:X]
        weight.sort(key=lambda edge: G[edge[0]][edge[1]]['weight'], reverse=True)
        sp_edges[0:X] = weight[0:X]

""" Shuffes edges. Then sorts probabilistically by smallest weight. """
def EDGE_Expovariate(G, sp_edges):
    random.shuffle(sp_edges)
    sp_edges.sort(key=lambda edge: random.expovariate(1000000000*G[edge[0]][edge[1]]['weight']), reverse=True)


def EDGE_avoidMakingBridges(G, sp_edges):
    num_bridges_after_removing_each_edge = {}
    for edge in sp_edges:
        H = G.copy()
        H.remove_edge(edge[0], edge[1])
        bridgeList = list(nx.bridges(H))
        num_bridges_after_removing_each_edge[edge] = len(bridgeList)

    #sp_edges.sort(key=lambda edge: random.expovariate(0.5*num_bridges_after_removing_each_edge[edge]), reverse=True)
    sp_edges.sort(key=lambda edge: num_bridges_after_removing_each_edge[edge], reverse=True)

    if len(sp_edges) > 1:
        spice = sp_edges[1:]
        random.shuffle(spice)
        test = random.uniform(0, 1)
        if test > 0.85:
            sp_edges[0] = spice[0]



def EDGE_SPtrueRandom(G, sp_edges):
    random.shuffle(sp_edges)



#### Completely random algorithm ####

""" Picks random set of edgeLimit edges to remove. Cannot disconnect graph. Tries 100 times. """
def EDGE_TrueRandom(G, edgeLimit):
    edges = G.edges()
    edgeLimit = min(edgeLimit, G.number_of_edges()-1)
    tries = 100
    while tries:
        to_remove = random.sample(edges, k=edgeLimit)
        H = G.copy()
        H.remove_edges_from(to_remove)
        if nx.is_connected(H):
            return to_remove
        else:
            tries -= 1
    return []


#### Brute force algorithm: Brute force all possibilities along SP edges. ####

def EDGE_SP_bruteforce(G, edgeLimit, target):
    if edgeLimit == 0:
        return []

    # 1. Calculate edges on SP that do not disconnect current graph.
    sp = shortestPath(G, target)
    sp_edges = [(sp[i], sp[i + 1]) for i in range(len(sp) - 1)]
    bridgeList = list(nx.bridges(G))
    sp_edges = [edge for edge in sp_edges if ((edge not in bridgeList) and (edge[::-1] not in bridgeList))]

    # 2. If no edges can be removed along SP without disconnecting graph, break loop. Can no longer improve.
    if not sp_edges:
        return []

    # 3.
    edgeDict = {}
    for edge in sp_edges:
        H = G.copy()
        H.remove_edge(edge[0], edge[1])

        optimal_removed = EDGE_SP_bruteforce(H, edgeLimit - 1, target)
        H.remove_edges_from(optimal_removed)

        all_removed = [edge] + list(optimal_removed)
        edgeDict[tuple(all_removed)] = shortestPath(H, target)

    print(max(edgeDict, key=lambda x: edgeDict[x]))
    return list(max(edgeDict, key=lambda x: edgeDict[x]))
