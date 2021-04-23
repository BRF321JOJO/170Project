import sys
sys.path.append("./project-sp21-skeleton")
from parse import *
from shortestPath import shortestPath
import matplotlib.pyplot as plt

def main(inputFile, nodeLimit, edgeLimit):
    G = read_input_file("inputs/" + inputFile)
    return maximalShortestPath(G, nodeLimit, edgeLimit)

def maximalShortestPath(G, nodeLimit, edgeLimit):
    #Find shortest_path info on G
    source = 0
    target = G.number_of_nodes() - 1
    

    #Modify G into G_prime, to maximize shortest path

    for i in range(edgeLimit): #Remove edgeLimit edges
        shortest_path, shortest_path_length = shortestPath(G) #Calculate new shortest path in G
        edgeTupleList = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path) - 1)] #Convert shortest path to list of edges
        edgeList = [(edge[0], edge[1], G[edge[0]][edge[1]]) for edge in edgeTupleList] #Convert edgesTuples to edges
        edgeList.sort(key=lambda x: x[2]['weight'])

        for edge in edgeList: #Remove first edge that doesn't disconnect the graph
            if (edge not in nx.algorithms.bridges(G)):
                G.remove_edge(edge[0], edge[1])
                #print(edge[0], edge[1])
                break


    #Find shortest_path info on final G
    new_shortest_path, new_shortest_path_length = shortestPath(G)

    #Output information about shortest_path distance increase
    delta_gained = new_shortest_path_length - shortest_path_length
    print("The new shortest path is " + str(new_shortest_path_length))
    print("The new shortest path is " + str(delta_gained) + " distance longer")

    #Show new G
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()

    return new_shortest_path, new_shortest_path_length


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

