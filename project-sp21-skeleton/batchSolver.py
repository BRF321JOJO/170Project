import random
from parse import read_input_file, write_output_file, read_output_file
from utils import calculate_score
import glob
import sys
from solver import solve

# Specify files not to run...
small_skip = [2,4,9,18,21,22,24,26,27,28,31,38,44,47,48,49,51,52,53,56,57,60,63,67,74,75,80,84,85,89,92,93,94,95,100,103,105,114,120,125,129,133,139,141,144,147,151,154,158,159,161,164,166,168,170,174,176,177,178,179,183,186,187,188,190,194,195,196,198,199,201,205,208,209,210,211,212,213,215,221,224,227,230,233,235,236,245,246,253,254,259,263,264,271,277,280,288,292,300]
medium_skip = [18,24,31,35,48,49,51,53,54,60,67,75,85,89,100,120,129,133,135,139,164,166,167,174,176,179,186,188,194,195,196,198,199,208,212,215,221,222,227,233,236,262]
large_skip = [18,31,35,46,48,49,51,53,54,60,63,67,75,85,89,90,92,100,120,133,139,151,164,168,174,176,194,195,198,199,212,215,221,227,262]
small_skip_paths = ["inputs/small/small-" + str(x) + '.in' for x in small_skip]
medium_skip_paths = ["inputs/medium/medium-" + str(x) + '.in' for x in medium_skip]
large_skip_paths = ["inputs/large/large-" + str(x) + '.in' for x in large_skip]

if __name__ == '__main__':
    number_iters = int(sys.argv[1])  # Specifies the number of iterations to run per file

    overall_improvement = 0  # Counts the number of outputs improved

    folders = glob.glob('inputs/*')
    random.shuffle(folders)

    for folder in folders:  # Iterate through folders in inputs
        files = glob.glob(folder + "/*")
        random.shuffle(files)
        size = folder[7:]

        if size == "small":
            skip_paths = small_skip_paths
        elif size == "medium":
            skip_paths = medium_skip_paths
        else:
            skip_paths = large_skip_paths

        files = [x for x in files if x not in skip_paths]

        for file_path in files:  # Iterates through every file in every folder
            print("Begin processing {}".format(file_path))
            G = read_input_file(file_path)  # Reads in the next graph

            output_path = 'outputs/' + file_path[7:][:-3] + '.out'

            improvements = 0  # Counts the number of times this output improved
            total_path_increased = 0  # Tracks the total path increased for this output
            was_improvement = False

            for i in range(number_iters):
                v, e = solve(G, size)  # Calculates the list of vertices (v) and edges (e) to remove

                currBest_distance = read_output_file(G, output_path)
                this_distance = calculate_score(G, v, e)

                if currBest_distance < this_distance:
                    was_improvement = True
                    improvements += 1
                    total_path_increased += (this_distance - currBest_distance)
                    print("Output distance IMPROVED by: " + str(this_distance - currBest_distance))
                    print("NEW shortest path is length: " + str(this_distance))
                    write_output_file(G, v, e, output_path)

            if was_improvement:
                overall_improvement += 1

            if improvements:
                print("TOTAL TIMES OUTPUT IMPROVED: " + str(improvements))
                print("TOTAL DISTANCE IMPROVED BY: " + str(total_path_increased))

    print("TOTAL OUTPUTS IMPROVED: " + str(overall_improvement))
