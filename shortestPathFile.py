import networkx as nx


# Returns list of vertices in shortest path in G
def shortestPath(G, t):
    s = 0
    sp = nx.algorithms.shortest_paths.weighted.dijkstra_path(G, s, t)
    return sp


# Returns length of path in G
def pathLength(G, path):
    return nx.classes.function.path_weight(G, path, weight="weight")
