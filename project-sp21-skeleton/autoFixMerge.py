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
    for new_output in files:  # Iterates through every file to merge
        input_path = size + "/" + new_output[12:]
        input_path = input_path[:len(input_path)-4] + ".in"
        input_path = "inputs/" + input_path

        old_outputs = 'outputs/' + input_path[7:][:-3] + '.out'

        G = read_input_file(input_path)

        currBest_distance = read_output_file(G, old_outputs)
        this_distance = read_output_file(G, new_output)

        if currBest_distance >= this_distance:
            #print("Output distance IMPROVED by: " + str(this_distance - currBest_distance))
            #print("NEW shortest path is length: " + str(this_distance))
            print(new_output + " not improved")


