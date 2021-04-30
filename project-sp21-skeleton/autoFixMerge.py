import glob
import random

import sys
import os.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from parse import read_input_file, read_output_file, write_output_file

if __name__ == '__main__':
    size = sys.argv[1]

    files = glob.glob('mergeFolder/*')
    files.sort()

    improvements = 0

    for new_output in files:  # Iterates through every file to merge
        print("Begin processing {}".format(new_output))
        input_path = size + "/" + new_output[12:]
        input_path = input_path[:len(input_path)-4] + ".in"
        input_path = "inputs/" + input_path

        old_output = 'outputs/' + input_path[7:][:-3] + '.out'

        G = read_input_file(input_path)

        currBest_distance = read_output_file(G, old_output)
        this_distance = read_output_file(G, new_output)

        if currBest_distance < this_distance:
            improvements += 1

            print("Output distance IMPROVED by: " + str(this_distance - currBest_distance))
            currBest_file = open(old_output, "w")
            merge_file = open(new_output, "r")

            currBest_file.write(merge_file.read())

            currBest_file.close()
            merge_file.close()

    print("Merge finished! " + str(improvements) + " files improved.")