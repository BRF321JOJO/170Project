import sys
sys.path.append("./project-sp21-skeleton")
from parse import *
import networkx as nx
import matplotlib.pyplot as plt


def genMaxShortestPath(H, vertexLimit, edgeLimit):
    G = H.copy()
    target = G.number_of_nodes() - 1
    removed_nodes = VERTEXremoveHighestDegree(G, vertexLimit, target)
    removed_edges = EDGEremoveShortest(G, edgeLimit, target)
    return removed_nodes, removed_edges


def shortestPath(G, t):
    s = 0
    sp = nx.algorithms.shortest_paths.weighted.dijkstra_path(G, s, t)
    #sp_length = nx.classes.function.path_weight(G, sp, weight="weight")
    return sp#, sp_length



def VERTEXremoveHighestDegree(G, vertexLimit, target):
    removed_nodes = []
    for i in range(vertexLimit):  #Remove verexLimit vertices
        sp = shortestPath(G, target)  #Calculate new shortest path in G
        sp = sp[1:len(sp)-1]   #Don't consider s and t for removal
        sp.sort(reverse=True, key=lambda vertex: G.degree[vertex])  #Sort vertices by decreasing degree

        for vertex in sp:
            if vertex not in nx.articulation_points(G):  #If removing this vertex would not disconnect graph
                G.remove_node(vertex)
                removed_nodes.append(vertex)
                break

    return removed_nodes


def EDGEremoveShortest(G, edgeLimit, target):
    removed_edges = []
    for i in range(edgeLimit):  #Remove edgeLimit edges
        sp = shortestPath(G, target)  #Calculate new shortest path in G
        sp_edges = [(sp[i], sp[i+1]) for i in range(len(sp) - 1)]  #Convert shortest path to list of edges
        sp_edges.sort(key=lambda edge: G[edge[0]][edge[1]]['weight'])  #Sort edges by increasing weight

        update = False
        for edge in sp_edges:
            edgeReverse = (edge[1], edge[0])
            bridgeList = list(nx.bridges(G))
            if (edge not in bridgeList) and (edgeReverse not in bridgeList):  #If removing this edge would not disconnect graph
                update = True
                G.remove_edge(edge[0], edge[1])
                removed_edges.append(edge)
                break

        if not update:  #Break loop when shortest path cannot increase without disconnecting graph
            break

    return removed_edges



def main(inputFile, nodeLimit, edgeLimit):
    G = read_input_file("project-sp21-skeleton/inputs/" + inputFile)
    return genMaxShortestPath(G, nodeLimit, edgeLimit)

if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
