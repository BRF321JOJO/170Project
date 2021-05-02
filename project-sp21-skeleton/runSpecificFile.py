from parse import read_input_file, write_output_file, read_output_file
from utils import calculate_score
import sys
from solver import solve
import re

if __name__ == '__main__':
    number_iters = int(sys.argv[1])  # Specifies the number of iterations to run per file
    file = sys.argv[2]  # Specifies running certain file

    size = re.split('/', file)
    size = size[1]

    print("Begin processing {}".format(file))
    G = read_input_file(file)  # Reads in the next graph

    output_path = 'outputs/' + file[7:][:-3] + '.out'

    improvements = 0  # Counts the number of times this output improved
    total_path_increased = 0  # Tracks the total path increased for this output

    sum_distance = 0
    for i in range(number_iters):
        v, e = solve(G, size)  # Calculates the list of vertices (v) and edges (e) to remove

        currBest_distance = read_output_file(G, output_path)
        this_distance = calculate_score(G, v, e)
        sum_distance += this_distance

        print("AVERAGE DISTANCE: " + str(sum_distance / (i+1)) + "            THIS DISTANCE: " + str(this_distance))
        if currBest_distance < this_distance:
            improvements += 1
            total_path_increased += (this_distance - currBest_distance)
            print("Output distance IMPROVED by: " + str(this_distance - currBest_distance))
            print("NEW shortest path is length: " + str(this_distance))
            write_output_file(G, v, e, output_path)

    print("FINAL AVERAGE DISTANCE: " + str(sum_distance / number_iters))
    if improvements:
        print("TOTAL TIMES OUTPUT IMPROVED: " + str(improvements))
        print("TOTAL DISTANCE IMPROVED BY: " + str(total_path_increased))
    print("SHORTEST PATH: " + str(currBest_distance))