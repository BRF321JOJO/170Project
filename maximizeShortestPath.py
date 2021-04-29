import sys
sys.path.append("./project-sp21-skeleton")
from parse import *
import networkx as nx
import matplotlib.pyplot as plt


def genMaxShortestPath(H, vertexLimit, edgeLimit):
    G = H.copy()
    target = G.number_of_nodes() - 1
    removed_nodes = VERTEXremoveGreedyHighestDegree(G, vertexLimit, target)
    removed_edges = EDGEremoveBruteForce(G, edgeLimit, target)
    return removed_nodes, removed_edges


#Returns list of vertices in shortest path in G
def shortestPath(G, t):
    s = 0
    sp = nx.algorithms.shortest_paths.weighted.dijkstra_path(G, s, t)
    return sp


# Returns length of path in G
def pathLength(G, path):
    return nx.classes.function.path_weight(G, path, weight="weight")


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


def EDGEremoveBruteForce(G, edgeLimit, target):
    if edgeLimit == 0:
        return []

    # Function returns a list of edges to remove that maximizes the shortest path
    sp = shortestPath(G, target)
    sp_edges = [(sp[i], sp[i + 1]) for i in range(len(sp) - 1)]

    dict = {}
    update = False
    for edge in sp_edges:
        edgeReverse = (edge[1], edge[0])
        bridgeList = list(nx.bridges(G))

        if (edge not in bridgeList) and (edgeReverse not in bridgeList):
            update = True
            H = G.copy()
            H.remove_edge(edge[0], edge[1])

            # Recursive call returns list of edges to remove that maximizes the shortest path from graph with "edge" removed
            optimal_removed = EDGEremoveBruteForce(H, edgeLimit - 1, target)
            all_removed = [edge] + list(optimal_removed)

            H.add_edge(edge[0], edge[1])
            H.remove_edges_from(all_removed)
            dict[tuple(all_removed)] = shortestPath(H, target)

    if not update:
        return []

    return list(max(dict, key=lambda x: dict[x]))


def main(inputFile, nodeLimit, edgeLimit):
    G = read_input_file("project-sp21-skeleton/inputs/" + inputFile)
    return genMaxShortestPath(G, nodeLimit, edgeLimit)

if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
