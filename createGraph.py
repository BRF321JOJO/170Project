import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

V = 30
G.add_nodes_from([0, V-1])

e = (0, 1)
#G.add_edge(*e)

lollipop = nx.lollipop_graph(10, 20)
lobster = nx.random_lobster(20, 0.7, 0.7)

#nx.draw(G, with_labels=True, font_weight='bold')
#nx.draw(lollipop, with_labels=True, font_weight='bold')
nx.draw(lobster, with_labels=True, font_weight='bold')
plt.show()