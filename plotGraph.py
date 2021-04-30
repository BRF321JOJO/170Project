import networkx as nx
import sys
import matplotlib.pyplot as plt

sys.path.append("./project-sp21-skeleton")
from parse import read_input_file, read_output_file
from maximizeShortestPath import shortestPath, pathLength

if __name__ == '__main__':
    number = sys.argv[1]
    size = sys.argv[2]

    file_path = "savedInputs/inputs/" + size + "/" + size + "-" + number + ".in"
    G = read_input_file(file_path)

    path = 'project-sp21-skeleton/outputs/' + size + "/" + size + '-' + number + ".out"
    distance = read_output_file(G, path)

    target = G.number_of_nodes()-1
    print("Target is: " + str(target))
    print("Old imprvement: " + str(distance))

    # Manually remove edges
    H = G.copy()
    H.remove_edges_from([(9, 21),(27, 26),(33, 34),
    (2, 3), (19, 18),(23, 63),(59, 60),(10, 11),
    (34, 54),(53, 54),(23, 24),(35, 34),(43, 44)])
    oldSP = pathLength(G, shortestPath(G, target))
    newSP = pathLength(H, shortestPath(H, target))
    print("New improvement: " + str(newSP - oldSP))

    pos = nx.kamada_kawai_layout(H)
    nx.draw_networkx(H, pos)
    labels = nx.get_edge_attributes(H, 'weight')
    nx.draw_networkx_edge_labels(H, pos, edge_labels=labels)
    plt.show()



