import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_score
import sys
from os.path import basename, normpath
import glob

#NEW
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from maximizeShortestPath import genMaxShortestPath

def solve(G, nodeLimit, edgeLimit):
    """
    Args:
        G: networkx.Graph
    Returns:
        c: list of cities to remove
        k: list of edges to remove
    """
    return genMaxShortestPath(G, nodeLimit, edgeLimit)


# For testing a folder of inputs to create a folder of outputs, you can use glob (need to import it)
if __name__ == '__main__':
    inputs = glob.glob('inputs/*')
    for input_path in inputs:
        files = glob.glob(input_path + "/*")
        for file_path in files:

            G = read_input_file(file_path)
            size = input_path[7:]
            
            if size == "small":
                c, k = solve(G, 1, 15)
            elif size == "medium":
                c, k = solve(G, 3, 50)
            else:
                c, k = solve(G, 5, 100)
            
            
            assert is_valid_solution(G, c, k)
            print(file_path)
            distance = calculate_score(G, c, k)

            output_path = 'outputs/' + file_path[7:][:-3] + '.out'
            write_output_file(G, c, k, output_path)


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
