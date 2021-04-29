import networkx as nx
import matplotlib.pyplot as plt
from maximizeShortestPath import shortestPath

G = nx.Graph()
G.add_nodes_from([0, 6])
#0 is s, 1 is a, ..., 5 is e, 6 is t

G.add_edge(0, 1, weight=2)
G.add_edge(0, 3, weight=9)
G.add_edge(0, 4, weight=3)

G.add_edge(1, 4, weight=8)
G.add_edge(1, 3, weight=3)
G.add_edge(1, 2, weight=4)


G.add_edge(2, 6, weight=2)
G.add_edge(2, 3, weight=1)
G.add_edge(2, 5, weight=9)

G.add_edge(3, 4, weight=1)
G.add_edge(3, 5, weight=2)
G.add_edge(3, 6, weight=6)

G.add_edge(4, 5, weight=2)

G.add_edge(5, 6, weight=4)



#Testing removal of two edges to maximize shortest path

sp = shortestPath(G, 6)
sp_edges = [(sp[i], sp[i+1]) for i in range(len(sp) - 1)]

for edge1 in sp_edges:
    H = G.copy()
    H.remove_edge(edge1[0], edge1[1])

    sp2 = shortestPath(H, 6)
    sp2_edges = [(sp2[i], sp2[i + 1]) for i in range(len(sp2) - 1)]

    for edge2 in sp2_edges:
        I = H.copy()
        I.remove_edge(edge2[0], edge2[1])

        sp3 = shortestPath(I, 6)
        sp_length = nx.classes.function.path_weight(I, sp3, weight="weight")
        print("Removed " + str(edge1) + str(edge2))
        print("The shortest path is " + str(sp3))
        print(sp_length)


'''
#Testing removal of node to maximize shortest path
sp = shortestPath(G, 6)
sp_length = nx.classes.function.path_weight(G, sp, weight="weight")

sp = sp[1:len(sp)-1]  #Only considers removal for the non-s/t nodes

for node in sp:
    H = G.copy()
    H.remove_node(node)

    sp2 = shortestPath(H, 6)
    sp_length = nx.classes.function.path_weight(H, sp2, weight="weight")
    print("Removed " + str(node))
    print("The shortest path is " + str(sp2))
    print(sp_length)
'''


#Testing removal of each of the edges on the shortest path
#G.remove_edge(0, 4)
#G.remove_edge(4, 3)
#G.remove_edge(3, 2)
#G.remove_edge(2, 6)


#nx.draw(G, with_labels=True, font_weight='bold')
#plt.show()
