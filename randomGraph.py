import sys
import random
import networkx as nx
import matplotlib.pyplot as plt

def main(numVertices):
    G = nx.Graph()
    G.add_nodes_from([0, numVertices-1]) #TODO: Ensure the 0 index

    for vertex in range(numVertices):
        #List of vertices to connect to VERTEX
        takenVertices = [i for i in range(numVertices)]
        random.shuffle(takenVertices)
        #Remove self-loop
        takenVertices.remove(vertex)

        for edge in range(numVertices//2):
            G.add_edge(vertex, takenVertices[edge], weight=round(random.uniform(0.001, 99.999), 3))

    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()

    #Call parse on G
    #Return output

    #In command, pipe output to file


if __name__ == "__main__":
    main(int(sys.argv[1]))