import sys
sys.path.append("./project-sp21-skeleton")
from parse import *
import networkx as nx
from utils import calculate_score


def genMaxShortestPath(H, vertexLimit, edgeLimit):
    target = H.number_of_nodes() - 1

    solutions = []

    # Solution 1
    G = H.copy()
    e1 = EDGEremoveGreedyShortest(G, edgeLimit, target)
    v1 = VERTEXremoveGreedyHighestDegree(G, vertexLimit, target)
    solutions.append((v1, e1))

    # Solution 2
    G = H.copy()
    v2 = VERTEXremoveGreedyHighestDegree(G, vertexLimit, target)
    e2 = EDGEremoveGreedyShortest(G, edgeLimit, target)
    solutions.append((v2, e2))

    # Solution 3
    #Try repeated k=5 brute forces


    # Solution 4: Randomized
    # G = H.copy()
    # e4 = EDGEremoveRandomized(G, edgeLimit, target)
    # v4 = VERTEXremoveGreedyHighestDegree(G, vertexLimit, target)
    # solutions.append((v4, e4))

    #Maximize over the solutions
    return max(solutions, key=lambda x: calculate_score(H, x[0], x[1]))


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



def main(inputFile, nodeLimit, edgeLimit):
    G = read_input_file("project-sp21-skeleton/inputs/" + inputFile)
    return genMaxShortestPath(G, nodeLimit, edgeLimit)

if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
