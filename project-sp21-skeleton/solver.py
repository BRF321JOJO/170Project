import networkx as nx
from parse import read_input_file, write_output_file, read_output_file
from utils import is_valid_solution, calculate_score
import sys
from os.path import basename, normpath
import glob


import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from maximizeShortestPath import genMaxShortestPath


def solve(G, size):
    """
    Args:
        G: networkx.Graph
    Returns:
        c: list of cities to remove
        k: list of edges to remove
    """

    if size == "small":
        nodeLimit = 1
        edgeLimit = 15
    elif size == "medium":
        nodeLimit = 3
        edgeLimit = 50 
    else:
        nodeLimit = 5
        edgeLimit = 100 

    return genMaxShortestPath(G, nodeLimit, edgeLimit)


# For testing a folder of inputs to create a folder of outputs, you can use glob (need to import it)
if __name__ == '__main__':

    improvements = 0 # Counts the number of outputs improved

    inputs = glob.glob('inputs/*')
    for input_path in inputs:   #Iterate through folders in inputs
        files = glob.glob(input_path + "/*")
        for file_path in files:  #Iterates through every file in every folder

            print("Begin processing {}".format(file_path))
            G = read_input_file(file_path)  #Reads in the next graph
            
            #Calculates the list of vertices (v) and edges (e) to remove
            size = input_path[7:]
            v, e = solve(G, size)
            
            assert is_valid_solution(G, v, e)


            # Compare result to current output file. Only overwrite output if better.
            output_path = 'outputs/' + file_path[7:][:-3] + '.out'
            currBest_distance = read_output_file(G, output_path)
            #currBest_distance = -1 # DEBUG

            this_distance = calculate_score(G, v, e)

            if currBest_distance >= this_distance:
                print("Current output is better or equal to this output. No output file written.")
            else:
                improvements += 1
                print("Output distance IMPROVED by: " + str(this_distance - currBest_distance))
                print("NEW shortest path is length: " + str(this_distance))
                write_output_file(G, v, e, output_path)

    print("TOTAL OUTPUTS IMPROVED: " + str(improvements))

# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

# if __name__ == '__main__':
#     assert len(sys.argv) == 2
#     path = sys.argv[1]
#     G = read_input_file(path)
#     c, k = solve(G)
#     assert is_valid_solution(G, c, k)
#     print("Shortest Path Difference: {}".format(calculate_score(G, c, k)))
#     write_output_file(G, c, k, 'outputs/small-1.out')


# For testing a folder of inputs to create a folder of outputs, you can use glob (need to import it)
# if __name__ == '__main__':
#     inputs = glob.glob('inputs/*')
#     for input_path in inputs:
#         output_path = 'outputs/' + basename(normpath(input_path))[:-3] + '.out'
#         G = read_input_file(input_path)
#         c, k = solve(G)
#         assert is_valid_solution(G, c, k)
#         distance = calculate_score(G, c, k)
#         write_output_file(G, c, k, output_path)
