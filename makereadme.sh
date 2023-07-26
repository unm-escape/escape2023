#!/bin/bash
# bash script to create default readme files in each directory

# loop over each folder
for dir in `ls -d day*`; do

  #extract the day number and date from part of the directory filename
  day=${dir:3:2}
  aug=${dir:9:2}

  #print out the numbers to check it's working
  echo $day $aug

  # write the readme file (one line)
  echo "## Files for ESCAPE 2023 Day $day, August $aug" > $dir/README.md
done

