#!/bin/bash
#This script automates the generation of output files for input files for 
#the Spring 2021 CS170 coding project at UC Berkeley.

echo -e "BEGIN CREATING OUTPUT FILES..."

sizes=('small' 'medium' 'large')

for size in ${sizes[@]}; do     #Iterate through sizes
    for filename in $(find inputs/$size | cut -d "/" -f 3- | cut -d "." -f 1); do   #Loop through files. Isolate the name of the file
    echo "Creating: $filename.out"
    python solver.py $filename $size
    done
done

