import sys
sys.path.append("./project-sp21-skeleton")
from parse import read_input_file, read_output_file

if __name__ == '__main__':

    file_path = "project-sp21-skeleton/inputs/small/small-135.in"
    G = read_input_file(file_path)

    merge1_path = 'merge1.out'
    merge2_path = 'merge2.out'
    merge1_distance = read_output_file(G, merge1_path)
    merge2_distance = read_output_file(G, merge2_path)

    print("MERGE1: " + str(merge1_distance))
    print("Merge2: " + str(merge2_distance))

    if merge1_distance >= merge2_distance:
        print("MERGE1 file has a better distance")
    else:
        print("MERGE2 file has a better distance")

