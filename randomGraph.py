import sys
import random
import networkx as nx
import matplotlib.pyplot as plt


def main(numVertices) {
    G = nx.Graph()

    #TODO: Ensure the 0 index
    G.add_nodes_from([0, numVertices-1])

    for (vertex in range(numVertices)) {

        takenVerticies = {}

        for (edge in numVertices/2) {
            #TODO: Add edge weight to this
            randomVertex = random.randInt(numVertices)
            while (randomVertex) {
                
            }
            e = (vertex, randomVertex)
            G.add_edge(*e)
        }
    }   

    nx.draw(G, with_labels=True, font_weight='bold')
}




if __name__ == "__main__":
    main(sys.argv[0])