from parse import read_input_file, write_output_file, read_output_file
from utils import is_valid_solution, calculate_score
import glob

import sys
import os.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solver import solve


if __name__ == '__main__':
    number_iters = int(sys.argv[1])  # Specifies the number of iterations to run per file
    overall_improvement = 0  # Counts the number of outputs improved

    inputs = glob.glob('inputs/*')
    for input_path in inputs:  # Iterate through folders in inputs
        files = glob.glob(input_path + "/*")
        for file_path in files:  # Iterates through every file in every folder

            print("Begin processing {}".format(file_path))
            G = read_input_file(file_path)  # Reads in the next graph

            size = input_path[7:]
            output_path = 'outputs/' + file_path[7:][:-3] + '.out'

            improvements = 0  # Counts the number of times this output improved
            total_path_increased = 0  # Tracks the total path increased for this output
            was_improvement = False

            for i in range(number_iters):
                # print("Iteration: " + str(i + 1))

                v, e = solve(G, size)  # Calculates the list of vertices (v) and edges (e) to remove
                assert is_valid_solution(G, v, e)

                currBest_distance = read_output_file(G, output_path)
                this_distance = calculate_score(G, v, e)

                if not currBest_distance >= this_distance:
                    was_improvement = True
                    improvements += 1
                    total_path_increased += (this_distance - currBest_distance)
                    print("Output distance IMPROVED by: " + str(this_distance - currBest_distance))
                    print("NEW shortest path is length: " + str(this_distance))
                    write_output_file(G, v, e, output_path)

            if was_improvement:
                overall_improvement += 1
            print("TOTAL TIMES OUTPUT IMPROVED: " + str(improvements))
            print("TOTAL DISTANCE IMPROVED BY: " + str(total_path_increased))

    print("TOTAL OUTPUTS IMPROVED: " + str(overall_improvement))
